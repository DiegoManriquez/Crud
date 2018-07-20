from django.db import models

class Celular(models.Model):
	serie = models.IntegerField()
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=50)
	so = models.CharField(max_length=50)

	def __str__(self):
		return self.modelo

	def get_absolute_url(self):
		return reverse('celular_edit', kwargs={'pk': self.pk})
