from django.db import models

from authuser.models import User, Doctor

# Create your models here.
class MedicalNote(models.Model):
    patient = models.ForeignKey(User, related_name='notas_paciente',
                                on_delete=models.CASCADE)
    
    doctor = models.ForeignKey(Doctor, related_name='notas_doctor',
                               on_delete=models.CASCADE)
    
    creation_date = models.DateTimeField(verbose_name='Fecha de Creacion')

    note = models.TextField(verbose_name='Nota')


    def __str__(self):
        date_tmp = self.creation_date.date()
        return f'{date_tmp.strftime("%d-%b-%Y")}: Dr. {self.doctor.get_short_name} - Paciente: {self.patient.get_full_name()}'


    class Meta:
        verbose_name = 'Medical Note'
        verbose_name_plural = 'Medical Notes'
