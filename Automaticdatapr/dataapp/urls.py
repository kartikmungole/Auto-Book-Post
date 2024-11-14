from django.urls import path
from . import views

urlpatterns = [
    path('submit-fake-book/', views.create_and_submit_book, name='submit_fake_book'),
]
