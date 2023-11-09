from django.db import models


class Products(models.Model):
    product_name = models.CharField('Наименование', max_length=100)
    vendor_code = models.CharField('Артикул', max_length=20)
    category = models.CharField('Категория', max_length=40)
    sub_category = models.CharField('Подкатегория', max_length=40)
    product_type = models.CharField('Вид изделия', max_length=40)
    completeness = models.CharField('Комплектность', max_length=40)
    gender = models.CharField('Пол', max_length=20)
    season = models.CharField('Сезон', max_length=20)
    material = models.CharField('Ткань/Материал верха', max_length=40)
    compound = models.CharField('Состав', max_length=20)
    density = models.CharField('Плотность/Толщина материала', max_length=20)
    color = models.CharField('Цвет', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


