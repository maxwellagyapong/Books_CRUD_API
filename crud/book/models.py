from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(_("Book Title"), max_length=100, unique=True)
    author = models.CharField(_("Author"), max_length=100, unique=False)
    year = models.IntegerField(_("Year Published"))

    def __str__(self):
        return self.title