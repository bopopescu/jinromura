from django.shortcuts import render,get_object_or_404
from .models import Village,Character
from django.views import generic

# Create your views here.
#初期検索・一覧画面
class IndexView(generic.ListView):
    model = Village
    template_name = 'jinromura/index.html'

    def get_queryset(self):
        #人数順に昇順、デフォルト全件取得
        village_list=self.model.objects.all().order_by('people')

        q_people = self.request.GET.get('people')

#peopleがnullのとき""を返すため
        if q_people != "":
            #検索を繰り返す時に全件から絞り込みを行う
            village_list =self.model.objects.all().order_by('people').filter(people=q_people)

        return village_list

class DetailView(generic.DetailView):
    model = Village
    template_name = 'jinromura/detail.html'
