from django.urls import path

from .views import ErrorListView, RecordNewError, AppDetailView, RegisterApp, AppsListView

urlpatterns = [
    path('', AppsListView.as_view(), name='apps_list'),
    path('all_errors', ErrorListView.as_view(), name='error_list'),
    path('<int:pk>/', AppDetailView.as_view(), name='app_detail'),
    path('<int:id>/error_log/', RecordNewError.as_view(), name='new_error'),
    path('register_app/', RegisterApp.as_view(), name='register_app'),
]
