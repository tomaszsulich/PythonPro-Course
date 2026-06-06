from dataclasses import dataclass
from enum import Enum, auto, IntEnum

class HTTP_METHODS(Enum):
    GET = auto()
    POST = auto()
    PUT = auto()
    DELETE = auto()
    
class HTTP_CODES(IntEnum):
    GET_OK = 200
    CREATED = 201
    NOT_FOUND = 404
    
@dataclass
class HttpResp:
    code: int
    data: dict


class FakeServer:
    """Symuluje serwer przetwarzający żądania klienta na uproszczonej bazie użytkowników."""
    
    def __init__(self):
        self.__next_id = 3
        self.db = {"users": [{"id": 1, "name": "Jan"}, 
                             {"id": 2, "name": "Anna"}]
                   }
        
    def handle_request(self, request: dict) -> HttpResp:
        """Kieruje żądanie do właściwej metody obsługi na podstawie metody HTTP."""
        # server/users
        
        """{'method': HTTP_METHODS,
        
        }
        """
        method = request["method"]
        
        if method == HTTP_METHODS.GET:
            return self.__get(request)
            
        elif method == HTTP_METHODS.POST:
            return self.__post(request)
        
        return HttpResp(
            HTTP_CODES.NOT_FOUND,
            {}
        )
            
    def __get(self, request: dict) -> HttpResp:
        """Obsługuje żądania GET, zwracając listę osób albo pojedynczy zasób."""
        
        # GET server/users -> wszystkich użytkowników
        p: str = request["path"]
        
        if p == "/users":
            return HttpResp(HTTP_CODES.GET_OK, {"users": self.db["users"]})
        # GET server/users/{id} -> zwracamy konkretnego użytkownika
        
        if p.startswith("/users/"):
            try:
                user = self.__db_user_by_id(int(p.rsplit("/", 1)[1]))
                return HttpResp(HTTP_CODES.GET_OK, user)
            except (ValueError, StopIteration):
                return HttpResp(HTTP_CODES.NOT_FOUND, {})
            
        return HttpResp(HTTP_CODES.NOT_FOUND, {})
                
    def __post(self, request: dict) -> HttpResp:
        """Obsługuje żądania POST, tworząc nowego użytkownika na podstawie danych z żądania."""
        
        p: str = request["path"]
        
        if p == "/users":
            nuser = self.__db_user_create(request["data"]["name"])
            return HttpResp(
                HTTP_CODES.CREATED,
                nuser
            )
            
        return HttpResp(HTTP_CODES.NOT_FOUND, {})
                
    def __db_user_create(self, name: str) -> dict:
        """Dodaje nowy rekord użytkownika do wewnętrznej bazy danych serwera."""
        
        nuser = {"id": self.__next_id,
                "name": name}
        self.db["users"].append(nuser)
        self.__next_id += 1
        return nuser
            
    def __db_user_by_id(self, id: int) -> dict:
        """Odszukuje rekord użytkownika na podstawie klucza głównego."""
        
        for user in self.db["users"]:
            if user["id"] == id:
                return user
        raise StopIteration
    
class FakeClient:
    """Symuluje klienta wysyłającego żądania do wskazanego serwera."""
        
    def send(self, server: FakeServer, request: dict) -> HttpResp:
        """Przekazuje żądanie do serwera i prezentuje otrzymaną odpowiedź."""
        
        response = server.handle_request(request)
        print(response)
        return response
    
    
def main() -> None:
    server = FakeServer()
    client = FakeClient()
    
    client.send(
        server, 
        {
            "method": HTTP_METHODS.GET,
            "path": "/users"
        },
    )
    
    client.send(
        server,
        {
            "method": HTTP_METHODS.POST,
            "path": "/users",
            "data": {"name": "Tomek"},
        },
    )
    
    client.send(
        server,
        {
            "method": HTTP_METHODS.GET,
            "path": "/users",
        },
    )
    
    client.send(
        server,
        {
            "method": HTTP_METHODS.GET,
            "path": "/atributes",
        },
    )
    
    
if __name__ == "__main__":
    main()