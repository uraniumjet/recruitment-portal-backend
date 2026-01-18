from django.urls import path
from .api_views import JobListCreateView, JobListCreateView,  JobDetailView

# urlpatterns = [
#     path("", JobListCreateView.as_view(), name="api-job-list"),
#     path("", JobListCreateView.as_view(), name="api-job-list"),
#     path("<int:pk>/", JobDetailView.as_view(), name="api-job-detail"),
# ]
urlpatterns = [
    path("", JobListCreateView.as_view(), name="api-job-list"),
    path("<int:pk>/", JobDetailView.as_view(), name="api-job-detail"),
    
]