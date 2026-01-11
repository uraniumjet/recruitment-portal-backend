from django.urls import path
from .views import (
    ApplyToJobView,
    MyApplicationsView,
    UpdateApplicationStatusView
)

urlpatterns = [
    path('jobs/<int:job_id>/apply/', ApplyToJobView.as_view()),
    path('applications/me/', MyApplicationsView.as_view()),
    path('applications/<int:pk>/', UpdateApplicationStatusView.as_view()),
]
