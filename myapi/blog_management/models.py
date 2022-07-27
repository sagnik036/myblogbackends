from email.mime import image
from django.db import models
from myapi.models import User
# Create your models here.
CHOICES = (
    ("1", "Mental Health"),
    ("2", "Heart Disease"),
    ("3", "Covid19"),
    ("4", "Immunization"),
)

def upload_path(instance ,filename):
    return '/'.join(['images',str(instance.title),filename])

class Myblog(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete = models.DO_NOTHING
    )
    title = models.CharField(
        max_length = 7,
        null = False,
        blank=False
    )
    image = models.ImageField(
        null = True,
        blank = True,
        upload_to = upload_path
    )
    catagory = models.CharField(
        max_length = 20,
        choices = CHOICES,
        null = False,
        blank = False
    )
    summary = models.CharField(
        max_length = 15
    )
    content = models.TextField(
        max_length=100
    )

    is_draft = models.BooleanField(
        default = False,
        null = True,
        blank = True
    )

    def __str__(self):
        return f"{self.user_id}"+ " " + f"{self.title}" 