from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('add_ninja/<int:id>', views.add_ninja),
    path('add_dojo', views.add_dojo),
    path('dojo/<int:id>', views.dojo_members),
    path('dojo/delete/<int:id>', views.delete_dojo),
    path('ninja/delete/<int:id>', views.delete_ninja),
]
