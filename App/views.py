from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import genshinstats as gs

# Create your views here.
@csrf_exempt
def login(request): 
    if request.method == "POST": 
        ltuid = json.loads(request.body)['ltuid']
        ltoken = json.loads(request.body)['ltoken']
        uid = json.loads(request.body)['uid']
        gs.set_cookie(ltuid=ltuid, ltoken=ltoken)

        return JsonResponse({
            "ltuid": ltuid, 
            "ltoken": ltoken, 
            "uid": uid, 
            "isAuth": True
        })
    
    return HttpResponse(False)

@csrf_exempt
def getCharacter(request): 
    if request.method == "POST": 
        ltuid = json.loads(request.body)['ltuid']
        ltoken = json.loads(request.body)['ltoken']
        uid = json.loads(request.body)['uid']
        gs.set_cookie(ltuid=ltuid, ltoken=ltoken)

        return JsonResponse(gs.get_characters(uid), safe=False)
    
    return JsonResponse({
        "status": False, 
        "message": "ltuid or ltoken or UID is incorrect"
    })