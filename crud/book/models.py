from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(_("Book Title"), max_length=100, unique=True, blank=False, null=False)
    author = models.CharField(_("Author"), max_length=100, unique=False, blank=False, null=False)
    year = models.DateField(_("Year Published"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title