from django.db import models
from django.utils import timezone

from authuser.models import Profile

# Create your models here.
class MedicalNote(models.Model):
    #patient = models.ForeignKey(User, related_name='notas_paciente',
    #                            on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, related_name='notas_paciente',
                              on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Paciente')
    
    #doctor = models.ForeignKey(Doctor, related_name='notas_doctor',
    #                           on_delete=models.CASCADE)
    
    creation_date = models.DateTimeField(default=timezone.now,
                                         verbose_name='Fecha de Creacion')

    note = models.TextField(verbose_name='Nota')


    def __str__(self):
        date_tmp = self.creation_date.date()

        if hasattr(self.owner, 'user'):
            information = f'{date_tmp.strftime("%d-%b-%Y")}: Dr. X - Paciente: {self.owner.user.get_full_name()}'
        else:
            information = f'{date_tmp.strftime("%d-%b-%Y")}: Dr. X - Paciente: USUARIO-ELIMINADO'

        return information


    class Meta:
        verbose_name = 'Medical Note'
        verbose_name_plural = 'Medical Notes'
