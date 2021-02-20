from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms import VisitorForm
from .filters import NewvisitorFilter
from django.http import JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render (request, "index.html",{})

@login_required(login_url='/login/')
def dash(request):
    return render(request, "dash.html", {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You have successfully login !'))
            return redirect("dash")
            #if request.user.groups.filter(name="field_office").exists():
                # user is an admin
                #return redirect("field_office")
            #else:
        else:
            messages.success(request, ('Invaild login'))
            return redirect('login')
    else:
        return render(request, "login.html",{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out !'))
    return redirect ('index')

@login_required(login_url='/login/')
def pastordash(request):
    members = crossroadmember.objects.all()
    visitors = newvisitor.objects.all()
    churches = NewChurches.objects.all()
    interns = Intern.objects.all()
    #date_visited = newvisitor.objects.all()

    total_members = members.count()
    total_visitor = visitors.count()
    total_planters = churches.count()
    total_interns = interns.count()

    covenant_members = members.filter(status='Covenant Member').count()
    regular_visitor = members.filter(status='Regular Visitor').count()
    left = members.filter(status='left').count()
    new_visitor=visitors.filter(status='New Visitor').count()
    planting = churches.filter(status='Alive').count()
    interns = interns.filter(status='Active').count()
    myFilter = NewvisitorFilter(request.GET, queryset=visitors)
    visitors = myFilter.qs

    context = {'members':members,'churches':churches, 'planting':planting, 'interns':interns, 'visitors':visitors,'covenant_members':covenant_members,
    'left':left,'regular_visitor':regular_visitor,'new_visitor':new_visitor, 'myFilter':myFilter}
    return render(request, "pastordash.html", context)

def visitor(request, id, *args, **kwarrgs):
    visitors = newvisitor.objects.get(id=id)
    #visitors.objects.filter(id=id).order_by('-id')

    return render(request, "visitor.html", {'visitors': visitors})

    #visitors = newvisitor.objects.all()
    #context = {'visitors':visitors}
    #return render (request, "test.html",{})

def newvisitors(request):
    visitors = newvisitor.objects.all()

    myFilter = NewvisitorFilter(request.GET, queryset=visitors)
    visitors = myFilter.qs

    context = {'visitors':visitors,'myFilter':myFilter}
    return render (request, "newvisitors.html",context)

def plant(request, id, *args, **kwarrgs):
    churches = NewChurches.objects.get(id=id)

    return render(request, "plant.html", {'churches': churches})

def New_Churches(request):
    churches = NewChurches.objects.all()

    #myFilter = NewvisitorFilter(request.GET, queryset=visitors)
    #visitors = myFilter.qs

    context = {'churches':churches}
    return render (request, "churchplant.html", context)


def newintern(request):
    interns = Intern.objects.all()

    context = {'interns':interns}
    return render (request,'newintern.html', context)


def interns(request, id, *args, **kwarrgs):
    interns = Intern.objects.get(id=id)

    return render(request, "interns.html", {'interns': interns})


def testing(request):
    return render (request, "testing.html",{})


#def resultsData(request, obj):
    #visitors = newvisitor.objects.all()
    #visitorsdata = []

    #new_visitor=visitors.filter(status='New Visitor').count()
    #date_visited = newvisitors.date_visited.all()

    #for i in date_visited:
        #visitorsdata.append({i.choice_text:i.votes})

    #print(visitorsdata)
    #return JsonResponse(visitorsdata, safe=False)
