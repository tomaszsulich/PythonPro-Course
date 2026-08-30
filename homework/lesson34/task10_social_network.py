import strawberry
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class User:
    id: strawberry.ID
    name: str

    @strawberry.field
    def posts(self) -> list["Post"]:
        return [post for post in fake_posts_db if post.author_id == self.id]


@strawberry.type
class Post:
    id: strawberry.ID
    title: str
    author_id: strawberry.Private[strawberry.ID]

    @strawberry.field
    def author(self) -> User:
        return next(user for user in fake_users_db if user.id == self.author_id)


fake_users_db = [
    User(id=strawberry.ID("1"), name="Jan Kowalski"),
    User(id=strawberry.ID("2"), name="Anna Nowak"),
]

fake_posts_db = [
    Post(
        id=strawberry.ID("1"),
        title="Pierwszy post",
        author_id=strawberry.ID("1"),
    ),
    Post(
        id=strawberry.ID("2"),
        title="Drugi post",
        author_id=strawberry.ID("1"),
    ),
    Post(
        id=strawberry.ID("3"),
        title="Trzeci post",
        author_id=strawberry.ID("2"),
    ),
]


@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> list[User]:
        return fake_users_db

    @strawberry.field
    def posts(self) -> list[Post]:
        return fake_posts_db


schema = strawberry.Schema(query=Query)

app = web.Application()
app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema),

)


if __name__ == "__main__":
    print("🚀 GraphQL API działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)