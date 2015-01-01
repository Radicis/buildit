from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import Page, Row, Column, Code

#Return a blank row with 1 column
def makeRow(page):
	page = Page.objects.get(id=page.id)
	row = Row(rel_page = page)	
	row.save()	
	column = Column(rel_row = row)	
	column.save()
	row.columns.add(column)	
	row.save()
	
	return row

#Generate a blank template with 1 row with 1 column	
def createPage():
	
	page = Page(title="Default")	
	page.save()	
	
	row = makeRow(page)
	
	page.rows.add(row)	
	page.save()
	
	return page

#create a row and add it to the page	
def addRow(request, page_id=1):
	page = Page.objects.get(id=page_id)
	row = makeRow(page)
	page.rows.add(row)
	page.save()
	
	return HttpResponseRedirect('/')
	
def deleteRow(request, row_id=1):
	row = Row.objects.get(id=row_id)
	row.delete()
	return HttpResponseRedirect('/')

def addCol(request, row_id=1):
	row = Row.objects.get(id=row_id)
	column = Column(rel_row=row)	
	column.save()	
	row.columns.add(column)
	row.save()
	
	return HttpResponseRedirect('/')
	
def deleteCol(request, column_id=1):
	col = Column.objects.get(id=column_id)
	col.delete()
	return HttpResponseRedirect('/')	

def home(request):
	
	page = Page.objects.all()
	
	page = page[0]
	
	return render(request, 'index.html', {'page':page})
