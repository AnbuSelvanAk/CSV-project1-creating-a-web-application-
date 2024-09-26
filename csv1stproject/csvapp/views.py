from django.shortcuts import render
import csv
from django.http import HttpResponse
NAME=['abdul','bala','dinesh','arjun']
SUB=['tamil','english','maths','science','computer']
AGE=[25,24,26,25,28]

def store(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=file.csv'
	writer=csv.writer(response)
	writer.writerow(['name','age','subject'])
	for(name,age,subject) in zip (NAME,AGE,SUB):
		writer.writerow([name,age,subject])
	return response