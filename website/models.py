from django.db import models

class Code(models.Model):
	html = models.CharField(max_length=1000) 
	
class Column(models.Model):
	html = models.ManyToManyField(Code, null=True)
	rel_row = models.ForeignKey('Row', null=True)

class Row(models.Model):
	columns = models.ManyToManyField(Column, null=True)
	rel_page = models.ForeignKey('Page', null=True)

class Page(models.Model):
	title = models.CharField(max_length=200)
	rows = models.ManyToManyField(Row, null=True)
