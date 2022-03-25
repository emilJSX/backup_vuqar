from django.urls import path

from . import views

app_name = 'blogapp'

urlpatterns = [
    path('bloq/<int:pk>/', views.BloqDetailView.as_view(), name="blog-detail")
]