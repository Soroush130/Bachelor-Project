from django.db import models


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
    rate = models.IntegerField(
        default=0
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


class Gallery(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='gallery/'
    )

    class Meta:
        db_table = 'gallery'

