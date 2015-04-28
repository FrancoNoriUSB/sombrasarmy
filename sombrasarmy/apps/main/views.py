# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.template import Context
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q
from datetime import datetime, date
from models import *
from forms import *


#Vista para el Pre-Home de Sombras Army
def pre_home(request):

	ctx={

	}

	return render_to_response('main/pre-home/pre-home.html', ctx, context_instance=RequestContext(request))