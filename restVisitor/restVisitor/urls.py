"""restVisitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include('visitor_app.urls')),
    path('api/token/auth/', obtain_jwt_token),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


"""
$ curl -X POST -d "username=pruthvi&password=pruthvi@1998" 'http://127.0.0.1:8000/api/token/auth/'


curl -X POST -H "Content-Type: application/json" -d '{"username":"pruthvi","password":"pruthvi@1998"}' http://localhost:8000/api/token/auth/


token = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InBydXRodmkiLCJleHAiOjE1ODk0Njc3OTIsImVtYWlsIjoicHJ1dGh2aWJhcm90N0BnbWFpbC5jb20ifQ.r9RdMf6FW_m0ffEGyFhZ90DUzz7tZH2P144h8xeEKco

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InBydXRodmkiLCJleHAiOjE1ODk0Njc3OTIsImVtYWlsIjoicHJ1dGh2aWJhcm90N0BnbWFpbC5jb20ifQ.r9RdMf6FW_m0ffEGyFhZ90DUzz7tZH2P144h8xeEKco" http://localhost:8000/v1/visits

"""