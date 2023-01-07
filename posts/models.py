from django.db import models


class posts(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    desciption=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title