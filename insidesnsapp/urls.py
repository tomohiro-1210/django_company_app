from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, likefunc, readfunc, postCreate

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name='logout'),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('like/<int:pk>', likefunc, name='like'),
    path('read.<int:pk>', readfunc ,name='read'),
    path('create/', postCreate.as_view(), name='create')
]
