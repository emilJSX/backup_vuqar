from django.shortcuts import render
from homepage.models import SaytinBaşlığıİcon,SaytınBaşlığı,Footer,Loqo,MüştəriRəyləri, MüştəriRəyləri_ÜstMətn,Haqqımda
from service.models import Xidmətlər, Xidmətlər_ÜstMətn
from about.models import HaqqımızdaÜçSektoru
from contact.models import Telefon_Email_Mekan, Sosial_Şəbəkələr

def about(request):
    sosial = Sosial_Şəbəkələr.objects.all()
    sekilucsektor = HaqqımızdaÜçSektoru.objects.all()
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    musterireyleriustmetn = MüştəriRəyləri_ÜstMətn.objects.all()
    musterireyleri = MüştəriRəyləri.objects.all()
    haqqimda = Haqqımda.objects.all()
    serviceustmetn = Xidmətlər_ÜstMətn.objects.all()
    service = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    saytinbasligi = SaytınBaşlığı.objects.all()
    footer = Footer.objects.all()
    loqo = Loqo.objects.all()
    saytibbasligiicon = SaytinBaşlığıİcon.objects.all()

    context = {
        'sekilucsektor' : sekilucsektor,
        'loqo' : loqo,
        'footer' : footer,
        'sosial' : sosial,
        'saytibbasligiicon' : saytibbasligiicon,
        'saytinbasligi' : saytinbasligi,
        'service' : service,
        'haqqimda':haqqimda,
        'tel_mail_mekan': tel_mail_mekan,
        'serviceustmetn' : serviceustmetn,
        'musterireyleriustmetn' : musterireyleriustmetn,
        'musterireyleri' : musterireyleri,
    }
    return render(request, "about.html", context)
