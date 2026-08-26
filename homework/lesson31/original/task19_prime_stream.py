import asyncio
from collections.abc import AsyncIterator


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False

    return True


async def generate_primes() -> AsyncIterator[int]:
    number = 2

    while number <= 100:
        if is_prime(number):
            await asyncio.sleep(0.1)
            yield number

        number += 1


async def main() -> None:
    async for prime in generate_primes():
        print(prime)


if __name__ == "__main__":
    asyncio.run(main())