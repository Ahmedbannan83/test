from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST


class HomeView(View):
    def get(self, request,*args, **kwargs):

        context={
            "name":"Ahmed BANNAN",
            "adress":"Settat , Maroc",            

        }

        return render(request,"home.html",context)

class AboutView(View):
    def get(self,request,*args,**kwargs):
        context={
            "title":'About'
        }

        return render(request,"about.html",context)
    
class AllArticlesView(View):
    def get(self,request,*args,**kwargs):
        context={
            "allarticles": Article.objects.all(),
        }
        return render(request,"allarticles.html",context)  




class CreateArticlesView(View):
    def post(self, request, *args, **kwargs):        
        try:
            Article.objects.create(
                title=request.POST.get("title"),
                content=request.POST.get("desciption"))
            resp = {
                "status": "success",
            }            
        except Exception as e:
            print(e)
            resp = {
                "status": "failed",
            }
        return JsonResponse(resp)
       
