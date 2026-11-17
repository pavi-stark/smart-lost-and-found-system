from django.urls import path
from . import views

urlpatterns = [
    # Main project views (Chapter 8)
    path('', views.home, name='home'),
    path('report/<str:status>/', views.report_item, name='report_item'),
    path('search/', views.search_items, name='search'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('claim/<int:pk>/', views.claim_item, name='claim_item'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Practices (Chapter 7)
    path('items/', views.items_practice, name='items_practice'),
    path('practice-1/', views.practice_1, name='practice_1'),

    # Auth
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('demo-login/<str:username>/', views.demo_login, name='demo_login'),
]
