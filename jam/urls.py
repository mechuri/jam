from django.urls import path
from . import views

app_name = "jam"
urlpatterns = [
    path('create_project/', views.create_project, name="create_project"),
    path('<int:id>/create_jam/', views.create_jam, name="create_jam"),
    ####path('<int:jam_id>/<int:project_id>/create_jjam/', views.create_jjam, name="create_jjam"),
    path('show/', views.show, name="show"),
    path('detail/<int:id>', views.detail, name="detail"),    
]