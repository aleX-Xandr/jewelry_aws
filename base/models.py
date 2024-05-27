from django.db import models

from jewelry.models import BaseModel


class Page(BaseModel):
    slug = models.CharField('Slug', max_length=50)
    name = models.CharField('Name', max_length=50)
    text = models.TextField('Text', default='', blank=True)

    meta_title = models.CharField('Meta Title', max_length=50, blank=True)
    meta_text = models.TextField('Meta Text', blank=True)

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.name


class ContactRequest(BaseModel):
    name = models.CharField('Name', max_length=50)
    email = models.CharField('Email', max_length=50)
    message = models.TextField('Message')

    class Meta:
        verbose_name = 'Contact Request'
        verbose_name_plural = 'Contact Requests'

    def __str__(self):
        return self.name


class Contact(BaseModel):
    phone_label = models.CharField('Phone Label', max_length=100)
    phone = models.CharField('Phone', max_length=50)
    address = models.CharField('Address', max_length=100)
    worktime = models.TextField('Worktime (next line ;)')
    breaktime = models.TextField('Breaktime (next line ;)')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.address


class AboutImage(BaseModel):
    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image', upload_to='about_images', null=True)

    class Meta:
        verbose_name = 'About Us Image'
        verbose_name_plural = 'About Us Images'

    def __str__(self):
        return self.name
