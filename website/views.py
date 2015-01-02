from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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
	if row.type < 4:
		column = Column(rel_row=row)	
		column.save()	
		row.columns.add(column)
		row.type += 1
		row.save()
	
	return HttpResponseRedirect('/')
	
def deleteCol(request, column_id=1):
	col = Column.objects.get(id=column_id)
	row = Row.objects.get(id=col.rel_row.id)
	if row.type > 1:
		row.type -= 1
	row.save()
	col.delete()
	return HttpResponseRedirect('/')

def addCode(request, column_id=1):
	col = Column.objects.get(id=column_id)
	code = Code.objects.all()
	code = code[0]
	#allow adding duplicate code items in column. may not work
	#if code in col.html.all():
	#	code2 = code
	#	col.html.add(code2)
	col.html.add(code)
	col.save()
	return HttpResponseRedirect('/')
	
def addCode2(request, column_id=1):
	col = Column.objects.get(id=column_id)
	code = Code.objects.all()
	code = code[1]
	col.html.add(code)
	col.save()
	return HttpResponseRedirect('/')
	
def delCode(request, column_id=1):
	col = Column.objects.get(id=column_id)
	col.html.clear()
	return HttpResponseRedirect('/')
	
def reset(request):
	for page in Page.objects.all():
		for row in page.rows.all():
			row.delete()
	return HttpResponseRedirect('/')

def preview(request, page_id=1):
	page = Page.objects.get(id=page_id)
	return render(request, 'preview.html', {'page':page})
	
def home(request):
	
	page = Page.objects.all()
	
	if page[0]:
		page = page[0]
	else:
		page = createPage()		
	
	return render(request, 'index.html', {'page':page})
