from django.urls import path
from . import views

app_name = "jam"
urlpatterns = [
    path('create_project/', views.create_project, name="create_project"),
    path('create_jam/<int:id>', views.create_jam, name="create_jam"),
    path('detail/<int:id>', views.detail, name="detail"),    
]