from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.ListSnippets.as_view()),
    path('<int:pk>/', views.DetailSnippets.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
]
