from django.db import models

class SelectDateTime(models.Model):
    # Дата проведения рыбалки
    date = models.DateField(
        auto_now_add=False,
        verbose_name="Дата")
    # Время начала рыбалки
    time = models.TimeField(
        auto_now_add=False,
        default='00:00',
        verbose_name="Время")

