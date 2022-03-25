from django.shortcuts import render
from .models import *
from service.models import Xidmətlər
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from homepage.models import SaytinBaşlığıİcon,SaytınBaşlığı,Footer,Loqo
from django.views.generic import DetailView
from contact.models import Telefon_Email_Mekan, Sosial_Şəbəkələr

def blog(request):
    blog = Bloq.objects.all()
    sosial = Sosial_Şəbəkələr.objects.all()
    service = Xidmətlər.objects.all().order_by('-vaxt')[:4]
    tel_mail_mekan = Telefon_Email_Mekan.objects.all()
    saytinbasligi = SaytınBaşlığı.objects.all()
    footer = Footer.objects.all()
    loqo = Loqo.objects.all()
    saytibbasligiicon = SaytinBaşlığıİcon.objects.all()

    number_items = 3
    page = request.GET.get('page')
    paginator = Paginator(blog, number_items)
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
        'blog' : blog,
        'sosial' : sosial,
        'page_range' : page_range,
        'items' : items,
        'loqo' : loqo,
        'footer' : footer,
        'service' : service,
        'tel_mail_mekan' : tel_mail_mekan,
        'saytibbasligiicon' : saytibbasligiicon,
        'saytinbasligi' : saytinbasligi,
    }
    return render(request, "blog.html", context)

class BloqDetailView(DetailView):
    model = Bloq
    template_name = 'blog-single.html'
    context_object_name = 'bloging'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['saytinbasligi'] = SaytınBaşlığı.objects.all()
        context['footer'] = Footer.objects.all()
        context['blog'] = Bloq.objects.all()
        context['loqo'] = Loqo.objects.all()
        context['saytibbasligiicon'] = SaytinBaşlığıİcon.objects.all()
        context['tel_mail_mekan'] = Telefon_Email_Mekan.objects.all()
        context['sosial'] = Sosial_Şəbəkələr.objects.all()

        return context
