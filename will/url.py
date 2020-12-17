from django.urls import path
from .views import WillListView, WillDetailView, WillCreateView, WillUpdateView, WillDeleteView

urlpatterns = [
  path('', WillListView.as_view(), name='will_list'),
  path('<int:pk>/', WillDetailView.as_view(), name='will_detail'),
  path('new/', WillCreateView.as_view(), name='will_create'),
  path('<int:pk>/edit', WillUpdateView.as_view(), name='will_update'),
  path('<int:pk>/delete', WillDeleteView.as_view(), name='will_delete'),
]