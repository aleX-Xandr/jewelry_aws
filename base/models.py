from django.db import models

from jewelry.models import BaseModel


class Setting(BaseModel):
    contact_form_title = models.CharField('Contact Form Title', max_length=100, blank=True)
    contact_form_text = models.TextField('Contact Form Text', blank=True)
    contact_email = models.CharField('Contact Email', max_length=100)

    footer_address = models.TextField('Footer Address', blank=True)
    footer_copyright = models.CharField('Footer Copyright', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return 'Settings'

    @staticmethod
    def get_settings():
        settings = Setting.objects.filter()
        if settings:
            return settings.first()
        else:
            settings = Setting()
            settings.save()
            return settings

    def get_address(self):
        return self.footer_address.split(';')


class Social(BaseModel):
    name = models.CharField('Name', max_length=100)
    link = models.CharField('Link', max_length=255)
    icon = models.FileField('Icon', upload_to='social_icons')
    sort = models.IntegerField('Sort', default=0)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'
        ordering = ['sort']

    def __str__(self):
        return self.name


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
    image = models.ImageField('Image', upload_to='contact_images', null=True)
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

    def get_worktime(self):
        return self.worktime.split(';')

    def get_breaktime(self):
        return self.breaktime.split(';')


class AboutImage(BaseModel):
    name = models.CharField('Name', max_length=50)
    image = models.ImageField('Image', upload_to='about_images', null=True)
    sort = models.IntegerField('Sort', default=0)

    class Meta:
        verbose_name = 'About Us Image'
        verbose_name_plural = 'About Us Images'
        ordering = ['sort']

    def __str__(self):
        return self.name
