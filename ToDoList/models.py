from django.db import models
# In your app's models.py file

# In your app's models.py file

from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], default='medium')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
