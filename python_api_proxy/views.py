from django.http import HttpResponse
from . import dispacher
import json

def event_sub(request,event_id):
    Dispacher = dispacher.C42Dispacher('ba8ba2a610c933aa72cbcf52d0cd2587a5047759',252)
    return HttpResponse(json.dumps(Dispacher.prepare_response(event_id)),content_type="application/json")
