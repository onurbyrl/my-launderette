from django.shortcuts import render
from .models import Announcement

# Create your views here.

def announcements(request):
    announce = Announcement.objects.all().order_by("-importance")
    return render(request,"announcements.html",{"announcements" : announce})