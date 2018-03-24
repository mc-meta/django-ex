import os
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)
   

    logger.error('Something went wrong! (err)')
    logger.info('Something went good! (info)')
    logger.warn('Something went warn! (warn)')

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    logger.error('Something went wrong! (err)')
    logger.info('Something went good! (info)')
    logger.warn('Something went warn! (warn)')
    return HttpResponse(PageView.objects.count())
