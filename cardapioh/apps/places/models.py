from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        abstract = True


class Place(Base):
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='places', null=True, blank=True)

    class Meta:
        verbose_name = 'place'
        verbose_name_plural = 'places'


class Session(Base):
    name_english = models.CharField(max_length=300, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='sessions', null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.place}'

    class Meta:
        verbose_name = 'session'
        verbose_name_plural = 'sessions'


class Item(Base):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='data', null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    description_english = models.TextField(max_length=1024, null=True, blank=True)
    price = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    discount = models.PositiveSmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='items', null=True, blank=True)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('code',)
