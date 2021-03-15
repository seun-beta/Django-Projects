from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


class Advert(models.Model):
    title = models.CharField(
        max_length=256,
        help_text="Input the title of your advert",
        validators=[MinLengthValidator
                    (1, "Please input a title with one or more characters")]
    )
    price = models.DecimalField(decimal_places=7, max_digits=10)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
