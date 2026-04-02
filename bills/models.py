from django.db import models

class Bill(models.Model):
    bill_number = models.CharField(max_length=20)
    state = models.CharField(max_length=10)
    title = models.TextField()
    status = models.IntegerField()
    last_action_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bill_number} ({self.state})"