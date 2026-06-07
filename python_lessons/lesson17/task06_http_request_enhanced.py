from dataclasses import dataclass, field
from enum import StrEnum, auto

class HttpMethod(StrEnum):
    GET = auto() # "get"
    POST = auto() # "post"
    PUT = auto()
    DELETE = auto()
    PATCH = auto()

@dataclass
class HttpRequest:
    method: HttpMethod
    target: str
    headers: dict = field(default_factory=dict)
    body: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.method, HttpMethod):
            raise TypeError(
                "Wrong type of method attr. Expected HttpMethod."
            )

    def display(self) -> None:
        print("--- HTTP Request ---")
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")

        print("Headers:")

        if self.headers:
            for key, value in self.headers.items():
                print(f"{key}: {value}")
        else:
            print("(empty)")

        print("Body:")

        if self.body:
            print(self.body)
        else:
            print("(empty)")

        print("--------------------")