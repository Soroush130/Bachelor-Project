from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    title = models.CharField(
        max_length=255
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(
        max_length=255
    )

    class Meta:
        db_table = 'brand'

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    price = models.PositiveSmallIntegerField(
        default=0
    )
    inventory = models.PositiveIntegerField(
        default=0
    )
    main_image = models.ImageField(
        upload_to='gallery/main_image/',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.title

    @property
    def calculate_rate_product(self):
        result = self.rates.all().aggregate(Avg('rate'))['rate__avg']
        print(result)
        return round(result)


class Rate(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='rates'
    )
    rate = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        db_table = 'rate'


class Gallery(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='gallery/'
    )

    class Meta:
        db_table = 'gallery'
