from django.shortcuts import render
from homepage.models import SaytinBaşlığıİcon,SaytınBaşlığı,Footer,Loqo
from service.models import Xidmətlər
from .models import Telefon_Email_Mekan, Form_Şəkil, Sosial_Şəbəkələr
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def contact(request):
    sosial = Sosial_Şəbəkələr.objects.all()
    form_sekil = Form_Şəkil.objects.all()
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    saytinbasligi = SaytınBaşlığı.objects.all()
    service = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    footer = Footer.objects.all()
    loqo = Loqo.objects.all()
    saytibbasligiicon = SaytinBaşlığıİcon.objects.all()

    if request.method == 'POST':
        adtext = request.POST.get('adtext')
        telefon = request.POST.get('telefon')
        mal = request.POST.get('mal')
        subject = request.POST.get('subject')

        data = {
            'adtext': adtext,
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
        message = render_to_string('mail.html', data)
        send_mail(
            "Müştəri tərəfindən sizə mesaj gəlib",
            message,
            settings.EMAIL_HOST_USER,
            ['info@mammoloqcerrah.az'],  
            fail_silently=False, html_message=message
        )

    

    context = {
        'loqo' : loqo,
        'sosial' : sosial,
        'service' : service,
        'footer' : footer,
        'saytibbasligiicon' : saytibbasligiicon,
        'saytinbasligi' : saytinbasligi,
        'tel_mail_mekan' : tel_mail_mekan,
        'form_sekil' : form_sekil,
    }
    return render(request, "contact.html", context)