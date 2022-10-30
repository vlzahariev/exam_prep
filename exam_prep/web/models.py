from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models

from exam_prep.web.validators import validate_only_alphanumeric


# Create your models here.


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(MinLengthValidator(2),
                    validate_only_alphanumeric),
        unique=True,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        choices=MUSICS,
        max_length=MAX_LEN_GENRE,
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(validators.MinValueValidator(0.0),),
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('pk',)
