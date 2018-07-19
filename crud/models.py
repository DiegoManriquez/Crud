from django.db import models

class Celular(models.Model):
	n_serie = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=50)
	so = models.CharField(max_length=50)

	def __str__(self):
		return self.modelo
