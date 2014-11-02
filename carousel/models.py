# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import LinkFields

from wagtail.wagtailcore.models import Orderable


class CarouselItem(LinkFields):
    images = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField(
        "Embed URLs",
        blank=True
    )
    caption = models.CharField(
        max_length=255,
        blank=True
    )

    class Meta:
        abstract = True
