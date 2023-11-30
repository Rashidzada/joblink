
from django.urls import path,include
from .views import*
from .routers import*
# print(routers.Route.count)
urlpatterns = [
    path('',index,name="index"),
    path('api/',include(router.urls))
]
