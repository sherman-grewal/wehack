from django.shortcuts import render
from hackerhub.models import Hackathon

# Create your views here.

def index(request):
    return render(request, 'hackerhub/index.html')

def hackathonList(request):
    
    hackathons = Hackathon.objects.order_by('startDate').reverse()
    template_name = 'hackerhub/hackathon_list.html'
    context = {
        'hackathons':hackathons,
    }

    return render(request, template_name, context)

