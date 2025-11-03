from django.shortcuts  import render
from .models import Elon

def asosiy (request):
    elonlar = Elon.objects.all().order_by('-sana')
    return render(request,  'asosiy.html', { 'elonlar': elonlar})
