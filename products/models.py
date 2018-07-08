from django.db import models
from django.contrib.auth.models import User

# product class
class product(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	pub_date = models.DateField()
	votes_total=models.PositiveIntegerField(default=1)
	image = models.ImageField(upload_to='images/')
	icon = models.ImageField(upload_to='images/')
	body = models.TextField(max_length=10000)
	hunter = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:300]