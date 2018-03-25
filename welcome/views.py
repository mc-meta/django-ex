import os
import sys
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Get an instance of a logger
root = logging.getLogger()
rooterr = logging.getLogger()
root.setLevel(logging.DEBUG)
rooterr.setLevel(logging.ERROR)

ch = logging.StreamHandler(sys.stdout)
cherr = logging.StreamHandler(sys.stderr) 
ch.setLevel(logging.DEBUG)
cherr.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
cherr.setFormatter(formatter)
root.addHandler(ch)
rooterr.addHandler(cherr)

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
   
    rooterr.err('Something went warn! (warn)')

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    root.err('Something went wrong! (err)')
    root.info('Something went good! (info)')
    root.warn('Something went warn! (warn)')
    return HttpResponse(PageView.objects.count())
