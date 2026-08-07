from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from drf_lab.views import (
    AuthorViewSet,
    BookViewSet,
    NoteViewSet,
    ProductViewSet,
    calculate,
    hello,
    set_name,
)


router = routers.DefaultRouter()

router.register(
    r"products",
    ProductViewSet,
)

router.register(
    r"notes",
    NoteViewSet,
)

router.register(
    r"authors",
    AuthorViewSet,
)

router.register(
    r"books",
    BookViewSet,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path(
        "api/",
        include(router.urls),
    ),
    
    path(
        "api/hello/",
        hello,
        name="hello",
    ),
    
    path(
        "api/set-name/",
        set_name,
        name="set_name",
    ),
    
    path(
        "api/calculate/",
        calculate,
        name="calculate",
    ),
]