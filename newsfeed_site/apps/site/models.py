# -*- encoding : utf-8 -*-

from django.db import models

class NewsPost(models.Model):
	date = models.DateField()
	title = models.CharField(max_length = 512)
	text = models.CharField(max_length = 2048)
	def unicode(self):
		return self.title + ": " + self.text