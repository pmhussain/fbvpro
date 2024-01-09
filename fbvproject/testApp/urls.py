from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.read), #read
    path('create', views.create), #insert
    path('update/<int:id>', views.update),
    path('delete/<str:id>', views.delete),
    #re_path(r'^update/(?P<id>\d+)$', views.update),
]
