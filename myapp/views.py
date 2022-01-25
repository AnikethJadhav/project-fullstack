from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

import json

from myapp.models import User 

# Create your views here.


def index(request):
  """
  Home Page
  """
  return render(request, 'myapp/index.html')


def list_records(request):
  """
  This function return the list of all the users.
  """
  users = User.objects.all().order_by("name")
  context = {"users": users}
  return render(request, 'myapp/records.html', context)


# Need to exempt csrf in order to extract the data because request.POST will contain only the data send through HTML <form> element.
@csrf_exempt
def save_record(request):
  """
  This extracts the data sent by client and stores it into our database iff it doen't exist.
  """
  new_user_data = json.loads(request.body)
  try:
    d = User.objects.get(email=new_user_data['email'])
    print(d)
    return JsonResponse({"status": False, "message": "User already exists"})
  except Exception as e:
    print(e)
  # print(data)
  new_user = User(**new_user_data)
  new_user.save()
  return JsonResponse({"status": True, "message": "Record saved successfully"})