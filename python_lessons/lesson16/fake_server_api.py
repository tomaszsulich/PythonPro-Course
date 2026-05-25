# POŁOWA ZADANIA 8, BO TRZEBA JESZCZE DOPISAĆ KLIENTA

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
    
    def __init__(self):
        self.__next_id = 2
        self.db = {"users": [{"id": 1, "name": "Jan"}, 
                             {"id": 2, "name": "Anna"}]
                   }
        
    def handle_request(self, request: dict):
        # server/users
        
        """{'method': HTTP_METHODS,
        
        }
        """
        method = request["method"]
        if method == HTTP_METHODS.GET:
            self.__get(request)
        elif method == HTTP_METHODS.POST:
            ...
            
    def __get(self, request: dict):
        # GET server/users -> wszystkich użytkowników
        p: str = request["path"]
        if p == "/users":
            return HttpResp(200, {"users": self.db["users"]})
        # GET server/users/{id} -> zwracamy konkretnego użytkownika
        if p.startswith("/users"):
            try:
                user = self.__db_user_by_id(int(p.rsplit("/", 1)))
                return HttpResp(HTTP_CODES.GET_OK, user)
            except ValueError:
                ...
            except StopIteration:
                return HttpResp(HTTP_CODES.NOT_FOUND, 
                                {})
                
    def __post(self, request: dict):
        p: str = request["path"]
        if p == "users":
            nuser = self.__db_user_create(request["data"]["name"])
            return HttpResp(HTTP_CODES)
                
    def __db_user_create(self, name: dict):
        nuser = {"id": self.__next_id,
                "name": name}
        self.db["users"].append(nuser)
        self.__next_id += 1
        return nuser
            
    def __db_user_by_id(self, id: int):
        for user in self.db["users"]:
            if user["id"] == id:
                return user
        raise StopIteration