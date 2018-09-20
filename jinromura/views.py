from django.shortcuts import render,get_object_or_404
from .models import Village,Character

# Create your views here.
#初期検索・一覧画面
def index(request):
    village_list = Village.objects.all()
    context={'village_list':village_list}
    return render(request, 'jinromura/index.html',context)

#検索
def get_query(self):
    #デフォルトは全件取得
    village_list = Village.objects.all()

    #GETのURLクエリパラメータ
    q_people = self.request.GET.getlist('people')

    if len(q_people)!= 0:
        village_list = village_list.filter(people__in=q_peoples)

    return render(request, 'jinromura/index.html',context)


#詳細画面
#URLの指定にvillage_idが必要なので追加
def detail(request,village_id):
    #オブジェクト（各々の村）取得か４０４エラー
    village = get_object_or_404(Village,pk=village_id)
    return render(request, 'jinromura/detail.html',{'village':village})
