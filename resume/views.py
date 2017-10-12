from django.shortcuts import render
from .models import People4,People3,People2,People
# Create your views here.
def index(request):
    people_list1=People.objects.all()
    people_list2 = People2.objects.all()
    people_list3 = People3.objects.all()
    people_list4 = People4.objects.all()

    return render(request,'base.html',context={'people_list1':people_list1,
                                               'people_list2':people_list2,
                                               'people_list3':people_list3,
                                               'people_list4':people_list4})