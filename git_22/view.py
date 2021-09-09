
from django.http import *

def index_view(request):
    return HttpResponse('hello')


