from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Job(models.Model):
    # 1. Define all your choices at the very top of the class
    JOB_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    # 2. Define your fields once
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField() # Changed to Integer as per your 2nd version
    
    job_type = models.CharField(
        max_length=20, 
        choices=JOB_TYPE_CHOICES
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    posted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        db_index=True
    )

    location = models.CharField(
        max_length=100,
        db_index=True
    )

    salary = models.IntegerField(db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title