from django.urls import path
from . import views


urlpatterns = [
    # set url path to home page index.html
    path('', views.home, name='index'),
    # set url path to create new account page
    path('create/', views.create_account, name='create'),
    # set url path to balance sheet page
    path('balance/', views.balance, name='balance'),
    # set url path to add new transaction page
    path('transaction/', views.transaction, name='transaction'),
    # set url path to add new balance sheet using a primary key
    path('<int:pk>/balance/', views.balance, name='balance'),
]
