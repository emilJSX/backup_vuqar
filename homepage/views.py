from django.shortcuts import render
from .models import *
from service.models import Xidmətlər, Xidmətlər_ÜstMətn
from blog.models import Bloq
from contact.models import Telefon_Email_Mekan
# Create your views here.

def homepage(request):
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    saytinbasligi = SaytınBaşlığı.objects.all()
    blog = Bloq.objects.all()
    saytibbasligiicon = SaytinBaşlığıİcon.objects.all()
    footer = Footer.objects.all()
    loqo = Loqo.objects.all()
    girishisse = Giriş_Hissə.objects.all()
    haqqimda = Haqqımda.objects.all()
    service = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    serviceustmetn = Xidmətlər_ÜstMətn.objects.all()
    asqebulayazilustmetn = AnaSəhifə_QəbulaYazıl_Mətnləri.objects.all()
    musterireyleriustmetn = MüştəriRəyləri_ÜstMətn.objects.all()
    musterireyleri = MüştəriRəyləri.objects.all()
    teztezverilensuallarustmetn = Tez_Tez_VerilənSuallarÜstMətn.objects.all()
    teztezverilensuallar = Tez_Tez_VerilənSuallar.objects.all()
    aboutmobileimg = MobileHaqqımızda.objects.all()
    context = {
        'saytinbasligi' : saytinbasligi,
        'saytibbasligiicon' : saytibbasligiicon,
        'footer' : footer,
        'loqo' : loqo,
        'girishisse' : girishisse,
        'haqqimda' : haqqimda,
        'asqebulayazilustmetn' : asqebulayazilustmetn,
        'musterireyleriustmetn' : musterireyleriustmetn,
        'musterireyleri' : musterireyleri,
        'teztezverilensuallarustmetn' : teztezverilensuallarustmetn,
        'teztezverilensuallar' : teztezverilensuallar,
        'service' : service,
        'tel_mail_mekan' : tel_mail_mekan,
        'blog' : blog,
        'serviceustmetn' : serviceustmetn,
        'aboutmobileimg' : aboutmobileimg,
    }
    return render(request, "index.html", context)


def sitemap(request):
    return render(request, 'sitemap.xml')

def robots(request):
    return render(request, 'robots.txt')
