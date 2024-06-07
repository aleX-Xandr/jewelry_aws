from django.db import models

from jewelry.models import BaseModel


class Category(BaseModel):
    slug = models.CharField('Slug', max_length=100)

    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image', upload_to='category_images')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')
    slug = models.CharField('Slug', max_length=100)
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')

    preview = models.ImageField('Preview', upload_to='product_previews')
    price = models.FloatField('Price')

    materials = models.ManyToManyField('Material', blank=True)
    quantity = models.IntegerField('Quantity', default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to='product_images')

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"{self.id}"


class Material(BaseModel):
    name = models.CharField('Name', max_length=50)
    color = models.CharField('Color (HEX)', max_length=10)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.name
