from ast import For
from django.shortcuts import render
from homepage.models import SaytinBaşlığıİcon,SaytınBaşlığı,Footer,Loqo
from .models import Form_Foto
from service.models import Xidmətlər
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from contact.models import Telefon_Email_Mekan, Sosial_Şəbəkələr
# Create your views here.

def appoinment(request):
    sosial = Sosial_Şəbəkələr.objects.all()
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    formfoto = Form_Foto.objects.all()
    saytinbasligi = SaytınBaşlığı.objects.all()
    footer = Footer.objects.all()
    loqo = Loqo.objects.all()
    service = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    saytibbasligiicon = SaytinBaşlığıİcon.objects.all()

    if request.method == 'POST':
        adtext = request.POST.get('adtext')
        soyad = request.POST.get('soyad')
        telefon = request.POST.get('telefon')
        mal = request.POST.get('mal')
        subject = request.POST.get('subject')

        data = {
            'adtext': adtext,
            'soyad' : soyad,
            'telefon': telefon,
            'mal': mal,
            'subject': subject,

        }
    #     adtext = '''
    #        Ad və Soyad: {}
    #        telefon: {}
    #        Email: {}
    #        Mesaj: {}
    #    '''.format(data['adtext'], data['telefon'], data['mal'], data['subject'])
        message = render_to_string('contactmail.html', data)
        send_mail(
            "Müştəri tərəfindən sizə mesaj gəlib",
            message,
            settings.EMAIL_HOST_USER,
            ['info@mammoloqcerrah.az'],  
            fail_silently=False, html_message=message
        )



    context = {
        'loqo' : loqo,
        'sosial': sosial,
        'service' : service,
        'tel_mail_mekan' : tel_mail_mekan,
        'footer' : footer,
        'saytibbasligiicon' : saytibbasligiicon,
        'saytinbasligi' : saytinbasligi,
        'formfoto' : formfoto,

    }
    return render(request, "appointment.html", context)
