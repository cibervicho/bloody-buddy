from django.db import models
from django.utils import timezone

from authuser.models import Profile

# Create your models here.
class Weight(models.Model):
    owner = models.ForeignKey(Profile, blank=True, null=True,
                              on_delete=models.SET_NULL, related_name='pesos',
                              verbose_name='Paciente')

    weight = models.FloatField(verbose_name='Peso (Kg)', blank=False, null=False)

    comments = models.TextField(verbose_name='Comentarios', blank=True, null=True,
                                editable=True)

    creation_date = models.DateTimeField(default=timezone.now,
                                       verbose_name='Fecha de Creacion')


    def __str__(self):
        date = self.creation_date.date()
        return f'{date.strftime("%d-%b-%Y")}: {self.owner.user.get_full_name()} - {self.weight} Kg'


    class Meta:
        verbose_name = 'Weight Record'
        verbose_name_plural = 'Weight Records'
