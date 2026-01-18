from django.urls import path
from .views import JobListCreateView,  JobDetailView, AdminJobApprovalView


urlpatterns = [
    path('', JobListCreateView.as_view(), name = 'jobs'),
    path('<int:pk>/', JobDetailView.as_view()),
    path('<int:pk>/approve/', AdminJobApprovalView.as_view()),
    

]

