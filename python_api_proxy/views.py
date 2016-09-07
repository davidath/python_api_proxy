from django.http import HttpResponse
from . import classes

def event_sub(request,event_id):
    Dispacher = classes.C42Dispacher('ba8ba2a610c933aa72cbcf52d0cd2587a5047759',252)
    return HttpResponse(event_id)
