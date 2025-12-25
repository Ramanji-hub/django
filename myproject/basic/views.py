from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import math
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import userprofile,Employee,MovieBooking,CourseRegistration



# Create your views here.

def getMovieTickets(request):
    try:
        if request.method == "GET":
            result = list(MovieBooking.objects.all().values())
            if len(result)==0:
                msg="no records found"
            else:
                msg="Data retrieved successfully"
            return JsonResponse({"status":"success","message":msg,"data":result,"total no.of records":len(result)})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})            
        


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

#httpresponse

def sample(request):
    qp1=request.GET.get('name')
    return HttpResponse("Hello Ramanji")

def sample1(request):
    return HttpResponse("<h1> WELCOME TO DJANGO <h1>")

def sample2(request):
    return JsonResponse({"data":[1,2,3]})

def sample3(request):
    return JsonResponse({"data":['frize','tv','washingmachine','cooler']})

def sample4(request):
    return JsonResponse([1,2,3,4],safe=False)

def sample5(request):
    info={'data':[{'name':'ramanji','age':22},{'name':'ramanji','age':22},{'name':'ramanji','age':22},{'name':'ramanji','age':22}]}
    return JsonResponse(info)

#I want to create  a view whih gives response as per my request.
#http methods:get,post,put/patch,delete
#get=> to retrive data from the server
#post=> to add/insert data from the server
#put/patch => to update the data through server
#delete=> to delete data through server

def sample6(request):
    qp1=request.GET.get('name')
    return HttpResponse(f"Hello {qp1}")

#dynamic response using query params
def productInfo(request):
    product_name=request.GET.get('product')
    quantity=request.GET.get('quantity')
    price=request.GET.get('price')
    data={'product':product_name,'quantity':quantity,'price':price}
    return JsonResponse(data)
# output
#it will give null
# {
#   "product": null,
#   "quantity": null,
#   "price": null
# }

def productInfo_default(request):
    product_name=request.GET.get('product','laptop')
    quantity=request.GET.get('quantity',2)
    price=request.GET.get('price',200)
    data={'product':product_name,'quantity':quantity,'price':price}
    return JsonResponse(data)

# output
# {
#   "product": "laptop",
#   "quantity": 2,
#   "price": 200
# }


#filtering using query params

def filteringData(request):
    data=[1,2,3,4,5,6,7,8,9]
    filteredData=[]
    qp=int(request.GET.get('nums',2))
    for x in data:
        if x%qp==0:
            filteredData.append(x)
    return JsonResponse({'data':filteredData})

students_data=[{'name':'ram','city':'hyd'},{'name':'venkat','city':'hyd'},{'name':'anji','city':'chennai'},{'name':'srinuvas','city':'chennai'}]
def filterStudentsByCity(request):
    filteredStudent=[]
    city=request.GET.get('city','hyd')
    for student in students_data:
        if student['city']==city:
            filteredStudent.append(student)
    return JsonResponse({'status':'success','data':filteredStudent})

x=['apple','banana','graphes','custard apple','pineapple','kiwi','Guvua','strawberry','watermelon','papaya','avacoda','carrot','bluebarry']
def pagination(request):
    page=int(request.GET.get('page',1))
    limit=int(request.GET.get('limit',3))

    start=(page-1)*limit
    end=page*limit
    total_pages=math.ceil(len(x)/limit)
    result=x[start:end]

    res={'status':"suscess",'page':page,"total_pages":total_pages,'data':result}

    return JsonResponse(res)

@csrf_exempt
def createData(request):
    if request.method=="POST":
        dataa=json.loads(request.body)
        print(dataa)
    return JsonResponse({"status":"Sucess","dataa":dataa})
    
@csrf_exempt
def createproduct(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
    return JsonResponse({"status":"Sucess","dataa":data})

@csrf_exempt
def own(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body) #dict
            name=data.get("name")
            age=data.get("age")
            city=data.get("city")
            userprofile.objects.create(name=name,age=age,city=city)
            print(data)
        return JsonResponse({"status":"Sucess","data":data})
    except Exception as e:
        return JsonResponse({"statuscode":500,"message":"internal server error"})

@csrf_exempt
def createEmployee(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            Employee.objects.create(emp_name=data.get("name"),emp_salary=data.get("salary"),emp_email=data.get("email"))
            print(data)
            
        return JsonResponse({"status":"success","data":data,"statuscode":201},status=201)
    except Exception as e:
        return JsonResponse({"status":"error","message":e},status=500)
    
@csrf_exempt  
def BookMyshow(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            MovieBooking.objects.create(moviename=data["movie_name"],showtime=data["show_time"],screenname=data["screen_name"])
            return JsonResponse({"status":"success","msg":"records inserted succesfully"})
        return JsonResponse({"status":"failure","message":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","message": str(e)}, status=500)
    

@csrf_exempt
def Stu_Reg(request):
    try:
        if request.method=="POST":
            data=json.loads(request.body)
            CourseRegistration.objects.create(name=data["Name"],email=data["Email"],course=data["Course"],phone=data["Phone"])
            return JsonResponse({"status":"success","msg":"Registration succesfully"})
        return JsonResponse({"status":"failed","msg":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":str(e)}, status=500)

#path parameters

student_info=[{"id":1,"name":"ram"},{"id":2,"name":"venkat"},{"id":3,"name":"veeranji"}]
def getStudentById(request,id):
    filteredStudent=[]
    for student in student_info:
        if id==student['id']:
            filteredStudent.append(student)
    return JsonResponse({"data":filteredStudent})

def student_reg(request):
    try:
        if request.method=="GET":
            result=list(CourseRegistration.objects.values())
            print(result)

            return JsonResponse({"status":"success","message":"data retrived successfully","data":result})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"Something went wrong"})

