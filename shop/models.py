from django.db import models

from jewelry.models import BaseModel


class Category(BaseModel):
    slug = models.CharField('Slug', max_length=100)

    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image', upload_to='category_images')

    sort = models.IntegerField('Sort', default=0)
    is_coulomb = models.BooleanField('Coulomb?', default=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['sort']

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

    sort = models.IntegerField('Sort', default=0)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['sort']

    def __str__(self):
        if 'oro giallo' in self.description:
            material = 'Gold'
        elif 'oro rosa' in self.description:
            material = 'Rose Gold'
        elif 'oro bianco' in self.description:
            material = 'Silver'
        else:
            material = ''
        return f"{self.name} {material}"

    def get_name(self):
        if len(self.name) > 15:
            return self.name[:15] + '...'
        return self.name

    def get_longer_name(self):
        if len(self.name) > 25:
            return self.name[:25] + '...'
        return self.name
    
    def is_ring(self):
        return 'anelli' in self.category.name.lower()

class ProductImage(BaseModel):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    material = models.ForeignKey('Material', on_delete=models.CASCADE, null=True)
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


class Bracelet(BaseModel):
    products = models.ManyToManyField('Product', blank=True)

    class Meta:
        verbose_name = 'Bracelet'
        verbose_name_plural = 'Bracelets'

    def __str__(self):
        return self.get_name()

    def get_price(self):
        sum = 0
        for product in self.products.all():
            sum += product.price
        return sum

    def get_name(self):
        return f"{len(self.products.all())} Coulons"
