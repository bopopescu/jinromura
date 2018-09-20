from django.shortcuts import render,get_object_or_404
from .models import Village,Character
from . import forms

# Create your views here.
#初期検索・一覧画面
def index(request):
    #人数順に昇順、デフォルト全件取得
    village_list = Village.objects.all().order_by('people')
    context={
    'village_list':village_list,
    'form':forms.SearchForm()
    }
    return render(request, 'jinromura/index.html',context)

#詳細画面
#URLの指定にvillage_idが必要なので追加
def detail(request,village_id):
    #オブジェクト（各々の村）取得か４０４エラー
    village = get_object_or_404(Village,pk=village_id)
    return render(request, 'jinromura/detail.html',{'village':village})
