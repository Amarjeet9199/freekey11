
from django.urls import path,include
from .views import (Freekey11Faq, Freekey11Features, Freekey11Home,Freekey11About,Freekey11About2, Freekey11Predictions,Freekey11Privacy, Freekey11Refund,Freekey11Contact, Freekey11Screenshots, prediction, Freekey11Terms)

urlpatterns = [
   
    path('', Freekey11Home.as_view(),name='home'),
    path('about', Freekey11About.as_view(),name='about'),
    path('privacy', Freekey11Privacy.as_view(),name='privacy'),
    path('refund', Freekey11Refund.as_view(),name='refund'),
    path('about2', Freekey11About2.as_view(),name='about2'),
    path('contact', Freekey11Contact.as_view(),name='contact'),
    path('predictions', Freekey11Predictions.as_view(),name='predictions'),
    path('paq', Freekey11Faq.as_view(),name='faq'),
    path('features', Freekey11Features.as_view(),name='features'),
    path('screenshots', Freekey11Screenshots.as_view(),name='screenshots'),
    path('terms', Freekey11Terms.as_view(),name='terms'),
    path('p1',prediction,name='predictions'),
]

