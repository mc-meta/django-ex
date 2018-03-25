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
root.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stderr)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
   

    root.error('Something went wrong! (err)')
    root.info('Something went good! (info)')
    root.warn('Something went warn! (warn)')

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    root.error('Something went wrong! (err)')
    root.info('Something went good! (info)')
    root.warn('Something went warn! (warn)')
    return HttpResponse(PageView.objects.count())
