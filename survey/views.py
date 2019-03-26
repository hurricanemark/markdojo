from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import SurveyItem

def surveyView(request):
	all_survey_items = SurveyItem.objects.all()
	return render(request, 'surveys.html', {'survey_items': all_survey_items})


def addSurvey(request):
	# create a new survey item, save, redirect browser to '/survey/'
	new_survey = SurveyItem(content = request.POST['content'])
	new_survey.save()  
	return HttpResponseRedirect('/survey/')

def deleteSurvey(request, survey_id):
	survey_to_delete = SurveyItem.objects.get(id=survey_id)
	survey_to_delete.delete()
	return HttpResponseRedirect('/survey/')