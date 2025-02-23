from django.db import models


class Contacts(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    def __str__(self):
        return f"{self.city}, {self.street}, {self.house_number}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    model = models.CharField(max_length=255, verbose_name='Модель продукта')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=0, verbose_name='Уровень иерархии')
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='customers',
                                 verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    contacts = models.OneToOneField(Contacts, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Контакты')
    products = models.ManyToManyField(Product, blank=True, verbose_name='Продукты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'
