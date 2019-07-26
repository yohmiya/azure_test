from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Recommend
from django.conf import settings

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


# レコメンドDBの表示用 view
def recommend_list(request):
    recommend = Recommend.objects.filter(available_flg='1').order_by('score_rank')
    page_obj = paginate_query(request, recommend, settings.PAGE_PER_ITEM)         # ページネーション
    return render(request, 'tmc_test/recommend_list.html', {'page_obj': page_obj}) # モデルから取得したobjectsの代わりに、page_objを渡す
    #return render(request, 'tmc_test/recommend_list.html', {})
