from django.urls import path
from .views import IndexView, TodoActivateView, logout_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:todo_id>/<str:action>/action/', TodoActivateView.as_view(), name='action'),
    path('logout/', logout_view, name='logout'),
]
