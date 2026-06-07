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
        if not self.validate_host_exists():
            raise ValueError("Host is required.")
        if not self.validate_uagent_exists():
            raise ValueError("User-agent is required.")
    
    # jeżeli przewidujemy, że hosta może częściej nie być, to lepiej na warunkach niż wyjątkach
    def validate_host_exists(self):
        if "host" in self.headers:
            return True
        return False
    
    def validate_uagent_exists(self):
        if "user-agent" in self.headers:
            return True
        return False
    
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