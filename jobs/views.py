from django.shortcuts import render
from .models import Job

# : sending jobs object 
# : Jobs app
# : home html
def nick(request):
   jobs = Job.objects 
   print(jobs)
   return render(request,'jobs/home.html',{'jobs':jobs})
   
