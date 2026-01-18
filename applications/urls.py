from django.urls import path
from .views import (
    ApplyToJobView,
    MyApplicationsView,
    UpdateApplicationStatusView
)

urlpatterns = [
    path('<int:job_id>/apply/', ApplyToJobView.as_view()),
    path('me/', MyApplicationsView.as_view()),
    path('int:pk>/', UpdateApplicationStatusView.as_view()),
]
