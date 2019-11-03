from django.db import models


class Report(models.Model):
    title = models.CharField(max_length=64, null=False)
    description = models.TextField(max_length=500, null=False)
    created_by = models.CharField(max_length=30, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)

    class Meta:
        db_table = 'reports'
