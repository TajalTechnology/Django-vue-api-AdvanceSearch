from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Division, District, Category, ChandaKatha


# Create your views here.
def product_list(request):
    return render(request, "model_main/base.html", )


def api_data(request):
    data = {
        'division': list(Division.objects.values()),
        'category': list(Category.objects.values()),
        # 'chandaKatha': list(ChandaKatha.objects.values())

    }
    return JsonResponse(data, safe=False)


def api_district(request):
    queryAll = District.objects
    if request.GET.get('division'):
        queryAll = queryAll.filter(division=request.GET.get('division'))

    district = queryAll.values()
    data = {
        'district': list(district),

    }
    return JsonResponse(data, safe=False)


def api_chandaKatha(request):
    queryAll = ChandaKatha.objects
    if request.GET.get('category'):
        queryAll = queryAll.filter(category=request.GET.get('category'))
    if request.GET.get('district'):
        queryAll = queryAll.filter(district=request.GET.get('district'))
    if request.GET.get('division'):
        queryAll = queryAll.filter(district_id=request.GET.get('division'))

    chandaKatha = queryAll.values('id', 'title', 'category_id', 'district_id', 'district__division_id',
                                  'category__name',
                                  'district__division__name', 'district__name')

    data2 = {
        'chandaKatha': list(chandaKatha)

    }
    return JsonResponse(data2, safe=False)
