import asyncio
from collections.abc import AsyncGenerator

import strawberry
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class User:
    id: strawberry.ID
    name: str


users: list[User] = []
registration_queue: asyncio.Queue[User] = asyncio.Queue()


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return users


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, name: str) -> User:
        user = User(
            id=strawberry.ID(str(len(users) + 1)),
            name=name,
        )

        users.append(user)
        await registration_queue.put(user)

        return user


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def user_registered(self) -> AsyncGenerator[User, None]:
        while True:
            user = await registration_queue.get()
            yield user


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
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