from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review'),
        ('Complete', 'Complete'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    completed = models.BooleanField(default=False)
    taskname= models.CharField(default=False)

    def __str__(self):
        return self.title
