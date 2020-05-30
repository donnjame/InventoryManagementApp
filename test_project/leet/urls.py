from django.urls import path
from . import views

app_name = 'leet'

urlpatterns = [
    path('',views.AssetListView.as_view(),name='list'),
    path('<int:pk>/',views.AssetDetailView.as_view(),name='detail'),
    path('users/', views.AnthemUserListView.as_view(),name='user_list'),
    path('users/<int:pk>', views.AnthemUserDetailView.as_view(),name='user_detail'),
    path('users/<int:pk>/', views.AssetDetailView.as_view(),name='asset_detail'),
    path('create/',views.AnthemAssetCreateView.as_view(),name='create'),
    path('createuser/',views.AnthemUserCreateView.as_view(),name='create_user'),
    path('delete/',views.AnthemAssetDeleteView.as_view(),name='delete_obj'),
    path('delete/<int:pk>',views.AnthemAssetDeleteView.as_view(),name='delete'),
    path('deleteuser/',views.AnthemUserDeleteView.as_view(),name='delete_user'),
    path('deleteuser/<int:pk>',views.AnthemUserDeleteView.as_view(),name='delete_user_pk'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('search/<int:pk>', views.SearchResultsView.as_view(), name='search_results_list'),
]
