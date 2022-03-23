from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from freekey11.models import Detail_View, ImgView

# Create your views here.
class Freekey11Home(TemplateView):
    template_name='index.html'

class Freekey11About(TemplateView):
    template_name='about.html'

class Freekey11About2(TemplateView):
    template_name='about2.html'

class Freekey11Privacy(TemplateView):
    template_name='privacy.html'
   
class Freekey11Refund(TemplateView):
    template_name='refund.html'

class Freekey11Contact(TemplateView):
    template_name='contact.html'

class Freekey11Predictions(TemplateView):
    template_name='predictions.html'

class Freekey11Faq(TemplateView):
    template_name='faq.html'

class Freekey11Features(TemplateView):
    template_name='features.html'    

class Freekey11Screenshots(TemplateView):
    template_name='screenshots.html'    

class Freekey11Terms(TemplateView):
    template_name='terms.html'     

def prediction(request):
    query = ImgView.objects.all()
    post = Detail_View.objects.all()
    context = {
        'quer':query,
        'pos':post
    }       
    return render(request,'predictions.html',context)    
       
   