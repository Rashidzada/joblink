from .viewsets import*
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user',UserViewSet)
router.register(r'author',AuthorViewSet)
router.register(r'book',BookViewSet)

