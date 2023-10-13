from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

#from authuser.models import User

# Create your models here.
class BloodPressureRecord(models.Model):
    user = models.ForeignKey(to="authuser.User",
                             on_delete=models.CASCADE)

    BLOOD_PRESSURE_TYPE_CHOICES = [
        ('No', 'Normal'),               # Sis < 120; Dia < 80 mmHg
        ('El', 'Elevada'),              # 119>Sis<130; Dia < 80 mmHg
        ('H1', 'Hipertension Fase 1'),  # 129>Sis<140; 79>Dia<90 mmHg
        ('H2', 'Hipertension Fase 2'),  # Sis > 139; Dia > 89 mmHg
    ]
    category = models.CharField(max_length=2, verbose_name='Categoria',
                                choices=BLOOD_PRESSURE_TYPE_CHOICES,
                                blank=True, null=True)

    sistolic = models.PositiveSmallIntegerField(verbose_name='Presion Arterial Sistolica (mmHg)',
                                                blank=False, null=False)
    diastolic = models.PositiveSmallIntegerField(verbose_name='Presion Arterial Diastolica (mmHg)',
                                                blank=False, null=False)

    # Heart Rate Limits: 60 > x < 190
    heart_rate = models.PositiveSmallIntegerField(verbose_name='Frecuencia Cardiaca (bpm)',
                                                  blank=True, null=True,
                                                  validators=[MaxValueValidator(500)])

    comments = models.TextField(verbose_name='Comentarios', blank=True, null=True,
                                editable=True)

    creation_date = models.DateTimeField(default=timezone.now,
                                       verbose_name='Fecha de Creacion')


    class Meta:
        verbose_name = 'Blood Pressure Record'
        verbose_name_plural = 'Blood Pressure Records'