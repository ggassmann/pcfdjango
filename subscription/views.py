from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt  
from .models import Subscription

def index(request):
  return HttpResponse('Subscription index.')

def read(request):
  return HttpResponse(
    serialize('json', Subscription.objects.all(), fields=('name', 'subscription_type', 'email_address')),
    content_type='application/json'
  )

#this is of course a security issue - I didn't realize django did this until I was already running a separate server for the frontend.
@csrf_exempt
def create(request):
  subscription = Subscription(
    name=request.POST.get('name'),
    email_address=request.POST.get('email'),
    subscription_type=request.POST.get('subscription')
  )
  try:
    subscription.full_clean()
    subscription.save()
    return JsonResponse(
      {"success": True}
    )
  except ValidationError as e:
    return JsonResponse(
      {"success": False, "error": e.message_dict},
      safe=False
    )