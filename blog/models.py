from django.db import models
from django.utils import timezone

#this line defines our model (it is an object). Post is the name of our model
#means that the Post is a Django Model, so Django knows that it should be saved in the database.
class Post(models.Model):
#ForeignKey is a link to another model
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#title is a text with limited number of characters
    title = models.CharField(max_length=200)
#text is the text :) unlimited characters
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
