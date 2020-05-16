from django.shortcuts import render
from django.views.generic import CreateView
from .models import InfoModel
from django.urls import reverse_lazy

# Create your views here.
def info(request):
    urls = InfoModel.objects.all()
    return render(request,'index.html',{'urls':urls})
class InfoRegister(CreateView):
    template_name = 'register.html'
    model = InfoModel
    fields = ('memo',)
    success_url = reverse_lazy('info')
