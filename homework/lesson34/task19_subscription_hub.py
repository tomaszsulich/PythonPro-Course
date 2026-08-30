import asyncio
from collections.abc import AsyncGenerator

import strawberry
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class User:
    id: strawberry.ID
    name: str


@strawberry.type
class Message:
    id: strawberry.ID
    content: str
    author: User


users = [
    User(id=strawberry.ID("1"), name="Anna"),
    User(id=strawberry.ID("2"), name="Jan"),
    User(id=strawberry.ID("3"), name="Maria"),
]

messages = [
    Message(
        id=strawberry.ID("1"),
        content="Czy ktoś tu jeszcze jest?",
        author=users[0],
    ),
    Message(
        id=strawberry.ID("2"),
        content="Pan WebSocket czuwa.",
        author=users[1],
    ),
]

message_queue: asyncio.Queue[Message] = asyncio.Queue()


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_message(self, content: str,
                           user_id: strawberry.ID) -> Message:
        user = next(
            (user for user in users if user.id == user_id),
            None,
        )

        if user is None:
            raise ValueError("Nie znaleziono użytkownika.")

        message = Message(
            id=strawberry.ID(str(len(messages) + 1)),
            content=content,
            author=user,
        )

        messages.append(message)
        await message_queue.put(message)

        return message


@strawberry.type
class Query:
    @strawberry.field
    def chat_history(self) -> list[Message]:
        return messages

    @strawberry.field
    def user(self, user_id: strawberry.ID) -> User | None:
        return next(
            (user for user in users if user.id == user_id),
            None,
        )


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def message_sent(self) -> AsyncGenerator[Message, None]:
        while True:
            message = await message_queue.get()
            yield message


schema = strawberry.Schema(
    mutation=Mutation,
    query=Query,
    subscription=Subscription,
)

app = web.Application()
app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema),
)


if __name__ == "__main__":
    print("🚀 GraphQL działa na http://localhost:8080/graphql")
    web.run_app(app, host="localhost", port=8080)