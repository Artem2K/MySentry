from django.urls import path

from .views import ErrorListView, ErrorDetailView

urlpatterns = [
    path('', ErrorListView.as_view(), name='error_list'),
    path('<int:pk>/', ErrorDetailView.as_view(), name='error_detail'),

]
