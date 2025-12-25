"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from basic.views import student_reg,Stu_Reg,getStudentById,getMovieTickets,createEmployee,own,createproduct,createData,home,about,sample,sample1,sample2,sample3,sample4,sample5,sample6,productInfo_default,filteringData,filterStudentsByCity,pagination, BookMyshow


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('sample/',sample),
    path('sample1/',sample1),
    path('sample2/',sample2),
    path('sample3/',sample3),
    path('sample4/',sample4),
    path('sample5/',sample5),
    path('sample6/',sample6),
    path('productInfo_default/',productInfo_default),
    path('filtering/',filteringData),
    path('student/',filterStudentsByCity),
    path('pagination/',pagination),
    path('create/',createData),
    path('createproduct/',createproduct),
    path('own/',own),
    path("emp/",createEmployee),
    path("bookticket/",BookMyshow),
    path("getMovieTickets/",getMovieTickets),
    path("getstudent/<int:id>",getStudentById),
    path("stu_reg/",Stu_Reg),
    path("student_reg/",student_reg)
]
