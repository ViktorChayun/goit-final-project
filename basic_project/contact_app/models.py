from typing import Optional
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, EmailValidator
from datetime import date


class Contact(models.Model):
    full_name: models.CharField = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(2, "Name must be at least 2 characters long")
        ]
    )
    address: models.CharField = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5, "Address must be at least 5 characters long")
        ]
    )
    email: models.EmailField = models.EmailField(
        validators=[EmailValidator("Enter a valid email address")]
    )
    phone: models.CharField = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+38 \(\d{3}\) \d{3}-\d{2}-\d{2}$',
                message="Phone number must be entered in the format: '+38 (XXX) XXX-XX-XX'. Up to 15 digits allowed."
            )
        ]
    )
    birthday: models.DateField = models.DateField()
    user: Optional[User] = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='contacts'
    )

    def clean(self) -> None:
        if self.birthday > date.today():
            raise ValidationError({'birthday': 'Birthday cannot be in the future'})

    def __str__(self) -> str:
        return self.full_name
