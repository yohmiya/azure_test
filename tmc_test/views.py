from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Recommend
from django.conf import settings
from . import forms
from django.db.models import Q

# ページネーション用関数の定義
def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

# TOP：検索画面用
def search_form(request):
    form = forms.SearchForm(request.GET or None)

    if form.is_valid():
        message = 'データ検証に成功しました'
    else:
        message = '検索ワードを入力してください。'

    d = {
        'form':form,
        'message':message,
    }

    return render(request, 'tmc_test/search_form.html', d)

# レコメンドDBの表示用（ほぼ全件） view
def recommend_list(request):
    recommend = Recommend.objects.filter(available_flg='1').order_by('poi_id')
    page_obj = paginate_query(request, recommend, settings.PAGE_PER_ITEM)         # ページネーション

    return render(request, 'tmc_test/recommend_list.html', {'page_obj': page_obj}) # モデルから取得したobjectsの代わりに、page_objを渡す
    #return render(request, 'tmc_test/recommend_list.html', {})

# レコメンドDBの表示用（施設名、住所の検索） view
def recommend_search_list(request):
    search_word = request.GET.get('search_text')
    recommend = Recommend.objects.filter(Q(poi__icontains=search_word) | Q(arr_an__icontains=search_word)).order_by('poi_id')
    page_obj = paginate_query(request, recommend, settings.PAGE_PER_ITEM)         # ページネーション

    return render(request, 'tmc_test/recommend_search_list.html', {'page_obj': page_obj}) # モデルから取得したobjectsの代わりに、page_objを渡す
