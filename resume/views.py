from django.shortcuts import render, get_object_or_404
from .models import People4, People3, People2, People
from django.db.models import Q


# Create your views here.
def index(request):
    people_list1 = People.objects.all()
    people_list2 = People2.objects.all()
    people_list3 = People3.objects.all()
    people_list4 = People4.objects.all()

    return render(request, 'base.html', context={'people_list1': people_list1,
                                                 'people_list2': people_list2,
                                                 'people_list3': people_list3,
                                                 'people_list4': people_list4})


def detail(request, pk):
    people = get_object_or_404(People, pk=pk)
    return render(request, 'myResume.html', {'people': people})


def detail2(request, pk):
    people2 = get_object_or_404(People2, pk=pk)
    return render(request, 'myResume.html', {'people': people2})


def detail3(request, pk):
    people = get_object_or_404(People3, pk=pk)
    return render(request, 'myResume.html', {'people': people})


def detail4(request, pk):
    people = get_object_or_404(People4, pk=pk)
    return render(request, 'myResume.html', {'people': people})


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = "输入关键字"
        return render(request, 'myResume.html', {'error_msg': error_msg})
    people_list = People.objects.filter(Q(name__icontains=q) | Q(message__icontains=q))
    people_list2 = People2.objects.filter(Q(name__icontains=q) | Q(message__icontains=q))
    people_list3 = People3.objects.filter(Q(name__icontains=q) | Q(message__icontains=q))
    people_list4 = People4.objects.filter(Q(name__icontains=q) | Q(message__icontains=q))
    return render(request, 'myResume.html', {'error_msg': error_msg,
                                         'people_list': people_list,
                                         'people_list2': people_list2,
                                         'people_list3': people_list3,
                                         'people_list4': people_list4})
