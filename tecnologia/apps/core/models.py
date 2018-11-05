from django.db import models

# Relacion persona 1 1 rol
class rol(models.Model):
    nombre_rol = models.CharField(max_length=30)

class persona(models.Model):
    idrol = models.ForeignKey(rol,on_delete=models.CASCADE)
    nombre_persona = models.CharField(max_length=100)
    apellido_persona = models.CharField(max_length=100)
    dni = models.CharField(max_length=9)
    contrasenha = models.CharField(max_length=9)

class tipoentrada(models.Model):
    descripcion = models.CharField(max_length=50)

class numeroentradas(models.Model):
    idtipoentrada = models.ForeignKey(tipoentrada,on_delete=models.CASCADE)
    area = models.FloatField()

class tipoconstruccion(models.Model):
    tipoedificacion = models.CharField(max_length=100)
    densidad = models.FloatField()
    area = models.FloatField()
    volumen = models.FloatField()
    orientacion = models.CharField(max_length=50)
    idnumeroentradas = models.ForeignKey(numeroentradas,on_delete=models.CASCADE)


class variables(models.Model):
    latitud = models.CharField(max_length=50)
    altitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    msnm = models.CharField(max_length=10)

class ambiente(models.Model):
    descripcion = models.CharField(max_length=50)

class sensorhumedad(models.Model):
    modelo = models.CharField(max_length=50)
    tipomedida = models.CharField(max_length=50)
    margenerrror = models.IntegerField()
    fechacompra = models.TimeField()

class lecturasensor(models.Model):
    idsensorhumeda = models.ForeignKey(sensorhumedad,on_delete=models.CASCADE)
    humedad = models.FloatField()
    temperatura = models.FloatField()
    momento = models.TimeField()

class persona_sensor(models.Model):
    idlecturasensor = models.ForeignKey(lecturasensor,on_delete=models.CASCADE)
    idvariable = models.ForeignKey(variables,on_delete=models.CASCADE)
    idtipoconstruccion = models.ForeignKey(tipoconstruccion,on_delete=models.CASCADE)
    idambiente = models.ForeignKey(ambiente,on_delete=models.CASCADE)
    fechainstalacion = models.DateField()
