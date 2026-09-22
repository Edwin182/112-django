from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# CREATE TABLE expenses (
#   id INTEGER AUTOINCREMENT PRIMARY KEY,
#   body VARCHAR(125),
#   age INTEGER
#)
class Post(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):      #toString
        return f"{self.title} by {self.author}"