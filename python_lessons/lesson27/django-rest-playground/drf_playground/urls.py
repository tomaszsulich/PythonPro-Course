from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, NoteViewSet, AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'notes', NoteViewSet)

router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls



# numbers = [1, 3, 10, 5, 5, 6, 11, 2, 25]

# def max_algo(array):
#     max(array[:2], array[0] + array[2])
    
# def calculator(num0, num1, op = "+"):
#     return num0 + num1