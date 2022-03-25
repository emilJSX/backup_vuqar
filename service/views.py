from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from homepage.models import SaytinBaşlığıİcon,SaytınBaşlığı,Footer,Loqo
from django.views.generic import DetailView
from contact.models import Telefon_Email_Mekan, Sosial_Şəbəkələr

# Create your views here.

def service(request):
    sosial = Sosial_Şəbəkələr.objects.all()
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    loqo = Loqo.objects.all()
    service = Xidmətlər.objects.all()
    service_footer = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    serviceustmetn = Xidmətlər_ÜstMətn.objects.all()

    number_items = 6
    page = request.GET.get('page')
    paginator = Paginator(service, number_items)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    index = items.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    page_range = paginator.page_range[start_index:end_index]
    context = {
        'service' : service,
        'tel_mail_mekan' : tel_mail_mekan,
        'serviceustmetn' : serviceustmetn,
        'loqo' : loqo,
        'sosial' : sosial,
        'items' : items,
        'service_footer' : service_footer,
        'page_range' : page_range,
    }
    return render(request, "service.html", context)



class XidmetlerDetailView(DetailView):
    model = Xidmətlər
    template_name = 'service-single.html'
    context_object_name = 'xidmet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saytinbasligi'] = SaytınBaşlığı.objects.all()
        context['tel_mail_mekan'] = Telefon_Email_Mekan.objects.all()
        context['footer'] = Footer.objects.all()
        context['loqo'] = Loqo.objects.all()
        context['saytibbasligiicon'] = SaytinBaşlığıİcon.objects.all()
        context['service'] = Xidmətlər.objects.all().order_by('-vaxt')[:4]
        context['sosial'] = Sosial_Şəbəkələr.objects.all()
        return context
