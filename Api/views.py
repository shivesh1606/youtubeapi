from django.shortcuts import render
from django.conf import settings
from .models import *
import requests
from django.http import HttpResponse, JsonResponse, Http404


# Create your views here.

def home(request):
    if request.method=="POST":
        search_url='https://www.googleapis.com/youtube/v3/search'
        params={
            'part' :'snippet',
            'q' : request.POST.get('keyword'),
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9
        }
        r=requests.get(search_url,params=params)
        results=r.json()['items']
        print(len(results))
        for result in results:
            try:
                a='https://www.youtube.com/embed/'+result['id']['videoId']
                v=Vedio.objects.create(link=a,title=result['snippet']['title'],description=result['snippet']['description'])
                v.save()
                print(v)
            except:
                pass
        msg='Search Successfull!!'
        context={
            'msg':msg,
            'vedio':Vedio.objects.all()   
        }
        return render (request,'base.html', context)
    else:
        return render(request,'base.html')

def getMessages(request, key):
    print(key)
    print('hghgf')
    search_url='https://www.googleapis.com/youtube/v3/search'
    params={
        'part' :'snippet',
        'q' : key,
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'maxResults': 9
    }
    r=requests.get(search_url,params=params)
    print(r)
    results=r.json()['items']
    print(results)
    length=0
    try:   
        length=len(Vedio.objects.filter(key=key))
    except:
        pass
    print(length)
    if length<100:
        for result in results:
            # try:
            a='https://www.youtube.com/embed/'+result['id']['videoId']
            v=Vedio.objects.create(key=key,link=a,title=result['snippet']['title'],date=str(result['snippet']['publishedAt'])[:10],description=result['snippet']['description'])
            v.save()
            print(v)
            # except:
            #     pass
        print('success')
        print(Vedio.objects.filter(key=key))
        # msg='Search Successfull!!'
        # context={
        #     'msg':msg,
        #     'vedio':Vedio.objects.all()   
        # }


    print(list(Vedio.objects.filter(key=key).order_by('date').values()))
    return JsonResponse({"messages":list(Vedio.objects.filter(key=key).order_by('date').values())})