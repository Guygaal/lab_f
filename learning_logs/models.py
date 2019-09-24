from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


MICRO_CHOICES = (
    ('MSUE', 'МПГУ'),
    ('MIPT', 'МФТИ'),
    ('IRE', 'ИРЭ'),
    ('OTHER', 'Другое'),
)

DRY_CHOICES = (
    ('HP', 'hot plate'),
    ('OVEN', 'oven'),
)
REF_CHOICES = (
    ('YES', 'Да'),
    ('NO', 'Нет'),
)


class Entry(models.Model):
    """Информация, изученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField(blank=True, null=True, verbose_name='Описание партии')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Название партии')
    microch = models.CharField(max_length=6, choices=MICRO_CHOICES, default='MSUE', verbose_name='Микроскоп')
    """----------------------Для МПГУ----------------------------------------------"""
    current = models.CharField(max_length=6,  blank=True, null=True, verbose_name='Ток, pA')
    voltage = models.CharField(max_length=3, blank=True, null=True, verbose_name='Ускоряющее напряжение, кВ')
    wd = models.CharField(max_length=4, blank=True, null=True, verbose_name='wd, мм')
    ss = models.CharField(max_length=3, blank=True, null=True, verbose_name='Spot Size')
    diaf = models.CharField(max_length=1, blank=True, null=True, verbose_name='Номер диафрагмы')
    hs = models.CharField(max_length=3, blank=True, null=True, verbose_name='hs')
    n = models.CharField(max_length=5, blank=True, null=True, verbose_name='n')
    """-----------------------Для МФТИ----------------------------------------------"""
    """current, voltage"""
    exp_time = models.CharField(max_length=10, blank=True, null=True, verbose_name='Время экспонирования в точке, мкс')
    dose = models.CharField(max_length=10, blank=True, null=True, verbose_name='Доза, мкКл/см^2')
    exp_size = models.CharField(max_length=10, blank=True, null=True,
                                verbose_name='Длина стороны квадрата поля экспонирования, мкм')
    num_dots = models.CharField(max_length=10, blank=True, null=True, verbose_name='Количество точек')
    micro_adv = models.TextField(blank=True, null=True, verbose_name='Дополнительно')
    """-----------------------Для ИРЭ----------------------------------------------"""
    """micro_adv"""
    """Другое"""
    resist = models.CharField(max_length=30, blank=True, null=True, verbose_name='Резист')
    resist_rpm = models.CharField(max_length=5, blank=True, null=True, verbose_name='Скорость нанесения, об/мин')
    resist_time = models.CharField(max_length=5, blank=True, null=True, verbose_name='Время нанесения, секунды')
    dry_type = models.CharField(max_length=6, choices=DRY_CHOICES, default='HP', verbose_name='Тип сушки')
    dry_temp = models.CharField(max_length=5, blank=True, null=True, verbose_name='Температура сушки, °C')
    dry_time = models.CharField(max_length=5, blank=True, null=True, verbose_name='Время сушки, секунды')
    dev = models.CharField(max_length=10, blank=True, null=True, verbose_name='Проявитель')
    dev_time = models.CharField(max_length=3, blank=True, null=True, verbose_name='Время проявки, секунды')
    ref = models.CharField(max_length=6, choices=REF_CHOICES, default='YES', verbose_name='Reflow')
    """YES"""
    ref_temp = models.CharField(max_length=5, blank=True, null=True, verbose_name='Температура reflow, °C')
    ref_time = models.CharField(max_length=5, blank=True, null=True, verbose_name='Время reflow, секунды')
    """------------------------------------------------------"""
    tr_rec = models.TextField(blank=True, null=True, verbose_name='Травление, рецепт')
    tr_time = models.CharField(max_length=5, blank=True, null=True, verbose_name='Время травления, секунды')
    tr_vel = models.CharField(max_length=5, blank=True, null=True, verbose_name='Скорость травления, нм/с')
    pyth = models.FileField(verbose_name="Python файл", upload_to='python/%Y/%m/%d', blank=True, null=True)
    gds = models.FileField(verbose_name="GDS файл", upload_to='gds/%Y/%m/%d', blank=True, null=True)
    body = models.TextField(blank=True, null=True, verbose_name='Дополнительное поле; изображения, таблицы')
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    date_added = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."

# Create your models here.
