from django.db import models


class Products(models.Model):
    vendor_code = models.CharField('Артикул', max_length=100)
    category = models.TextField('Категория')
    sub_category = models.TextField('Подкатегория')
    product_type = models.TextField('Вид изделия')
    completeness = models.TextField('Комплектность')
    gender = models.TextField('Пол')
    season = models.TextField('Сезон')
    material = models.TextField('Ткань/Материал верха')
    compound = models.TextField('Состав')
    density = models.TextField('Плотность/Толщина материала')
    color = models.TextField('Цвет')

    def __str__(self):
        return self.vendor_code

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


