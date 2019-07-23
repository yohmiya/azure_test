from django.shortcuts import render

# Create your views here.
def recommend_list(request):
    return render(request, 'tmc_test/recommend_list.html', {})
