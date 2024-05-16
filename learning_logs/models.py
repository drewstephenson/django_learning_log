from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """A class to represent a topic the user is learning about."""
    text = models.CharField(max_length=200)  # topic title can be up to 200 characters long
    date_added = models.DateTimeField(auto_now_add=True)  # adds the current date and time to uploaded topics
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # establishes a connection between a topic and a user

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """A class to represent something learned about a topic."""
    # ForeignKey() establishes a connection between a topic and each of its entries.
    # When the topic is deleted, CASCADE tells Django to delete all of its entries as well.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()  # similar to CharField, but for longer text entries
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."
    