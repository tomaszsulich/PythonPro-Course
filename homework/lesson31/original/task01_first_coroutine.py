import asyncio


async def study_ready() -> None:
    print("Gotowy do nauki asyncio!")


if __name__ == "__main__":
    asyncio.run(study_ready())