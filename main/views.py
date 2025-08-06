from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'index.html', {'todos': todos})  
    
    def post(self, request):
        body = request.POST.get('body')
        if body:
            Todo.objects.create(user=request.user, body=body)
        return redirect('index')