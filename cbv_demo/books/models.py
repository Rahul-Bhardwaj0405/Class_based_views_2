from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=50)
#     description = models.TextField()
#     is_published = models.BooleanField(default=True)

#     def __str__(self):
#         return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
