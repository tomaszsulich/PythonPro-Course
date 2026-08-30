import strawberry
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView
from strawberry.dataloader import DataLoader


@strawberry.type
class Post:
    id: strawberry.ID
    title: str


@strawberry.type
class User:
    id: strawberry.ID
    name: str

    @strawberry.field
    async def posts(self, info: strawberry.Info) -> list[Post]:
        return await info.context["posts_loader"].load(self.id)


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return fake_users_db


fake_posts_db = [
    {
        "id": "1",
        "title": "Wykorzystanie AI w grafice komputerowej",
        "author_id": "1"
    },
    {
        "id": "2",
        "title": "Wpływ gier komputerowych na współczesną młodzież",
        "author_id": "1"
    },
    {
        "id": "3",
        "title": "Analiza kampanii marketingowej Facebooka",
        "author_id": "2"
    },
    {
        "id": "4",
        "title": "Którym zawodom AI pomoże, a którym zaszkodzi?",
        "author_id": "3"
    },
]

fake_users_db = [
    User(id=strawberry.ID("1"), name="Anna"),
    User(id=strawberry.ID("2"), name="Jan"),
    User(id=strawberry.ID("3"), name="Maria"),
]


async def load_posts(user_ids: list[strawberry.ID]) -> list[list[Post]]:
    print(f"📦 DataLoader pobiera posty dla {user_ids}")

    return [
        [
            Post(
                id=strawberry.ID(post["id"]),
                title=post["title"],
            )
            for post in fake_posts_db
            if post["author_id"] == user_id
        ]
        for user_id in user_ids
    ]


class CustomGraphQLView(GraphQLView):
    async def get_context(self, request: web.Request,
                          response: web.StreamResponse) -> dict[str, DataLoader]:
        return {
            "posts_loader": DataLoader(load_fn=load_posts),
        }


schema = strawberry.Schema(query=Query)

app = web.Application()
app.router.add_route(
    "*",
    "/graphql",
    CustomGraphQLView(schema=schema),
)


if __name__ == "__main__":
    print("🚀 GraphQL działa na http://localhost:8080/graphql")
    web.run_app(app, host="localhost", port=8080)