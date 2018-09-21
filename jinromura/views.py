from django.shortcuts import render,get_object_or_404
from .models import Village,Character
from . import forms
from django.views import generic

# Create your views here.
#初期検索・一覧画面
class IndexView(generic.ListView):
    template_name = 'jinromura/index.html'

    def get_queryset(self):
        #人数順に昇順、デフォルト全件取得
        return Village.objects.all().order_by('people')

class DetailView(generic.DetailView):
    model = Village
    template_name = 'jinromura/detail.html'
