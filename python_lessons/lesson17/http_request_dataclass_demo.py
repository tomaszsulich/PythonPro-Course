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
    body: dict = field(default_factory=dict)
    
    def __post_init__(self):
        if not isinstance(self.method, HttpMethod):
            raise TypeError("Wrong type of method attr. Expected HttpMethod.")
        
    def display(self):
        print(f"""--- HTTP Request ---
            Method: {self.method}
            Target: {self.target}
            Headers:
            Host: example.com
            User-Agent: {self.headers.get("user-agent", "<empty>")}
            Body:
            (empty)
            --------------------""")
        
HttpRequest()