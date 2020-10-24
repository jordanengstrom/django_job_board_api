from django.db import models


class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=75)
    job_title = models.CharField(max_length=75)
    job_description = models.TextField(max_length=1500)
    salary = models.DecimalField(max_digits=6, decimal_places=0)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.job_title} at {self.company_name}'
