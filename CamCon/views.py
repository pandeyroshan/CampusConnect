from django.shortcuts import render,redirect
from .models import Notices,Chat
from django.contrib.auth.decorators import login_required
from .forms import ChatForm
import datetime
# Create your views here.

@login_required
def index(request):
    data = Notices.objects.all().order_by('-date')
    return render(request,'CamCon/home.html',{ 'dataset' : data})

@login_required
def chat(request):
    if request.method=='POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            ChatData = form.save(commit=False)
            ChatData.user = request.user
            ChatData.save()
        return redirect('chat')
    else:
        form = ChatForm()
        data = Chat.objects.all().order_by('-timeStamp')
        return render(request,'CamCon/chat.html',{'dataset': data, 'form':form})