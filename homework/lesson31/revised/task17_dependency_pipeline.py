import asyncio


async def fetch_user_id(username: str) -> int:
    await asyncio.sleep(1)
    return 42


async def fetch_posts(user_id: int) -> list[int]:
    await asyncio.sleep(1)
    return [101, 102, 103]


async def fetch_comments(post_id: int) -> list[str]:
    await asyncio.sleep(1)

    return [
        f"Komentarz 1 do posta {post_id}",
        f"Komentarz 2 do posta {post_id}",
    ]


async def main() -> None:
    username = "tomek"

    user_id = await fetch_user_id(username)
    posts = await fetch_posts(user_id)

    comments = await asyncio.gather(
        *(fetch_comments(post_id) for post_id in posts)
    )

    print(f"User ID: {user_id}")
    print(f"Posty: {posts}")

    for post_id, post_comments in zip(posts, comments):
        print(f"\nPost {post_id}:")

        for comment in post_comments:
            print(f"- {comment}")


if __name__ == "__main__":
    asyncio.run(main())