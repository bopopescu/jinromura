from django.shortcuts import render,get_object_or_404
from .models import Village,Character
from django.views import generic

# Create your views here.
#初期検索・一覧画面
class IndexView(generic.ListView):
    model = Village
    template_name = 'jinromura/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #人数順に昇順ソート
        context['village_list']= self.model.objects.all().order_by('people')

        return context

    #絞り込みボタンをクリックした時の表示
    def get_queryset(self):
        #人数順に昇順、デフォルト全件取得
        object_list = self.model.objects.all().order_by('people')

        q_people = self.request.GET.get('people')

        #indexの初期表示以外のとき
        if q_people is not None:
            #peopleがnullのとき
            if q_people != "":
                #検索を繰り返す時に全件から絞り込みを行う
                object_list =object_list.filter(people=q_people)

            context['village_list']= object_list

        return context

class DetailView(generic.DetailView):
    model = Village
    template_name = 'jinromura/detail.html'
