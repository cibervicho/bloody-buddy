from django.db import models
from django.utils import timezone


# Create your models here.
class Weight(models.Model):
    user = models.ForeignKey(to="authuser.User",
                             on_delete=models.CASCADE)

    weight = models.FloatField(verbose_name='Peso', blank=False, null=False)

    comments = models.TextField(verbose_name='Comentarios', blank=True, null=True,
                                editable=True)

    creation_date = models.DateTimeField(default=timezone.now,
                                       verbose_name='Fecha de Creacion')


    def __str__(self):
        date = self.creation_date.date()
        return f'{date.strftime("%d-%b-%Y")}: {self.weight} Kg'


    class Meta:
        verbose_name = 'Weight Record'
        verbose_name_plural = 'Weight Records'
