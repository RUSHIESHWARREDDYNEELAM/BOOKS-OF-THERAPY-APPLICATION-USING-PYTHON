from django.db import models 
class Contact(models.Model): 
name = models.CharField(max_length=122) 
email = models.CharField(max_length=122) 
phone = models.CharField(max_length=12) 
desc = models.TextField() 
date = models.DateField() 
def __str__(self): 
return self.name 
class Book(models.Model): 
title = models.CharField(max_length=255) 
cat = models.CharField(max_length=255) 
price = models.IntegerField() 
quant = models.IntegerField() 
image_url = models.CharField(max_length=2083) 
def __str__(self): 
return self.title 
class Fibuy(models.Model): 
email = models.CharField(max_length=255) 
address = models.CharField(max_length=255) 
phone = models.IntegerField() 
prod_id=models.CharField(null=True ,max_length=255) 
def __str__(self): 
return self.email 
class Sell(models.Model): 
prod_id = models.CharField(max_length=255) 
fname = models.CharField(max_length=255) 
money = models.IntegerField() 
16 address = models.CharField(max_length=255) 
phone = models.IntegerField() 
year = models.IntegerField() 
def __str__(self): 
return self.phone 
import os 
from django.contrib.messages import constants as messages 
from pathlib import Path 
# Build paths inside the project like this: BASE_DIR / 'subdir'. 
BASE_DIR = Path(__file__).resolve().parent.parent 
# Quick-start development settings - unsuitable for production 
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/ 
# SECURITY WARNING: keep the secret key used in production secret! 
SECRET_KEY = 'django-insecure-is78kf8)7ro8txos($1zrx*o9i!1i%vo7^9p*bs3#3$!8y%i-*' 
# SECURITY WARNING: don't run with debug turned on in production! 
DEBUG = True 
ALLOWED_HOSTS = [] 
# Application definition 
INSTALLED_APPS = [ 
'home.apps.HomeConfig', 
'django.contrib.admin', 
'django.contrib.auth', 
'django.contrib.contenttypes', 
'django.contrib.sessions', 
'django.contrib.messages', 
'django.contrib.staticfiles', 
] 
MIDDLEWARE = [ 
'django.middleware.security.SecurityMiddleware', 
'django.contrib.sessions.middleware.SessionMiddleware', 
17 
'django.middleware.common.CommonMiddleware', 
'django.contrib.auth.middleware.AuthenticationMiddleware', 
] 
ROOT_URLCONF = 'knowledge.urls' 
TEMPLATES = [ 
{ 
'BACKEND': 'django.template.backends.django.DjangoTemplates', 
'DIRS': [os.path.join(BASE_DIR, "templates")], 
'APP_DIRS': True, 
'OPTIONS': { 
'context_processors': [ 
'django.template.context_processors.debug', 
'django.template.context_processors.request', 
'django.contrib.auth.context_processors.auth', 
'django.contrib.messages.context_processors.messages', 
], 
}, 
}, 
] 
WSGI_APPLICATION = 'knowledge.wsgi.application' 
# Database 
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases 
DATABASES = { 
'default': { 
'ENGINE': 'django.db.backends.sqlite3', 
'NAME': BASE_DIR / 'db.sqlite3', 
} 
} 
# Password validation 
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators 
'django.middleware.common.CommonMiddleware', 
18 { 
'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', 
{ 
'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
}, 
{ 
'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', 
}, 
{ 
'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', 
}, 
] 
# Internationalization 
# https://docs.djangoproject.com/en/3.2/topics/i18n/ 
LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'UTC' 
USE_I18N = True 
USE_L10N = True 
USE_TZ = True 
# Static files (CSS, JavaScript, Images) 
# https://docs.djangoproject.com/en/3.2/howto/static-files/ 
STATIC_URL = '/static/' 
# Default primary key field type 
STATICFILES_DIR = [ 
os.path.join(BASE_DIR, "static") 
] 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' 
19HTML 
<div class="container my-4"> 
<div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel"> 
<div class="carousel-indicators"> 
<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" 
aria-current="true" aria-label="Slide 1"></button> 
<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria
label="Slide 2"></button> 
<button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria
label="Slide 3"></button> 
</div> 
<div class="carousel-inner"> 
<div class="carousel-item active"> 
<img src="https://source.unsplash.com/900x350/?book" class="d-block w-100" alt="..."> 
<div class="carousel-caption d-none d-md-block"> 
<h5 style=" background:black; border-radius:11px;">Welcome To The Shop Of Knowledge</h5> 
<p style=" background:black;border-radius:11px;">MADE BY ST-9 TEAM </p> 
</div> 
</div> 
<div class="carousel-item"> 
<img src="https://source.unsplash.com/900x350/?books" class="d-block w-100" alt="..."> 
<div class="carousel-caption d-none d-md-block"> 
<h5 style=" background:black;border-radius:11px;">Save Your Money And Increase Your 
Knowledge</h5> 
<p style=" background:black;border-radius:11px;">Buy,Sell Or Exchange Yours Books With Low 
Cost</p> 
</div> 
20 <img src="https://source.unsplash.com/900x350/?notebook" class="d-block w-100" alt="..."> 
<div class="carousel-caption d-none d-md-block"> 
<h5 style="background:black;border-radius:11px;"> 
Sky Is Not The Limit Of Knowledge </h5> 
<p style=" background:black;border-radius:11px;">Help US To Build ,Share The website</p> 
</div> 
</div> 
</div> 
<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data
bs-slide="prev"> 
<span class="carousel-control-prev-icon" aria-hidden="true"></span> 
<span class="visually-hidden">Previous</span> 
</button> 
<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data
bs-slide="next"> 
<span class="carousel-control-next-icon" aria-hidden="true"></span> 
<span class="visually-hidden">Next</span> 
</button> 
</div> 
</div> 
<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data
bs-slide="prev"> 
<span class="visually-hidden">Previous</span> 
</button> 
<button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data
bs-slide="next"> 
<span class="carousel-control-next-icon" aria-hidden="true"></span> 
<span class="visually-hidden">Next</span> 
</div> 
<h3 class="text-center" style="color:#d00b0b;"> THIS SITE IS CREATED BY ST-9 DJANGO 
,HTML,CSS,BOOTSTRAP</h3> 
{% endblock body %} 
21OPTIONS 
{% extends 'base.html'%} 
{% block body %} 
<div class="container-fluid my-3" > 
<div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel"> 
<div class="carousel-inner"> 
<div class="carousel-item active"> 
<img src="https://source.unsplash.com/900x300/?book" class="d-block w-100" alt="..."> 
</div> 
</div> 
</div> 
<h1 class="text-center" style="color:purple;"> BOOK AVAILABLE </h1> 
{% for home in cb %} 
<div class="col"></div> 
<div class="card" style="width: 28rem; my-5"> 
<div class="card-body"> 
<h5 class="card-title" style="color:#d00b0b;">BOOK: {{home.title}}</h5> 
<h6 class="card-text" style="color:#d00b0b;">STOCK: {{home.quant}}</h6> 
<h6 class="card-text" style="color:#b635f8;">PRICE: RS {{home.price}}</h6> 
<a href="/fibuy/{{home.id}}" class="btn btn-primary">BUY NOW</a> 
</div> 
</div>
