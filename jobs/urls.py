from django.urls import path
from .views import JobListCreateView,  JobDetailView, AdminJobApprovalView

urlpatterns = [
    path('jobs/', JobListCreateView.as_view(), name = 'jobs'),
    path('jobs/<int:pk>/', JobDetailView.as_view()),
    path('jobs/<int:pk>/approve/', AdminJobApprovalView.as_view()),

]
