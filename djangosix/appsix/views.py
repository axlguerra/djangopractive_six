from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View,  TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models
# Create your views here.


class Indexview(TemplateView):
    template_name= 'appsix/index.html'


    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['injectme']= 'basic injection'
        return context


class SchoolListview(ListView):
    model = models.School

class SchoolDetailview(DetailView):
    model = models.School

    template_name = 'appsix/school_details.html'

# class CBView(View):
#     def get(self, request):
#         return HttpResponse('CLASS BASE VIEWS ARE COOL!')

# def index(request):
#     return render(request, 'appsix/index.html')