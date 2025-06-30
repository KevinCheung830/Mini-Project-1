from django.shortcuts import render , HttpResponse


# Create your views here.
# In this view function, the request contains all the data the user sent through a browser. It is like 0.0.0.0 , all request from the sender. 

def pagerender(request):
    return HttpResponse( "Welcome to Ks app")

def user_list(request):
    return HttpResponse( "User list")

def user_add(request):
    return HttpResponse( "Add User")

def tablee(request):
    py_var=[
        {
            "name":"Andy",
            "Age":30,
            "Code":"Dobulase"
        },
        {
            "name":"Micheal",
            "Age":28,
            "Code":"Abisasa"
        },
        {
            "name":"Kasing",
            "Age":22,
            "Code":"Igamono"
        }
               ]
    return render(request,'tbl.html',{ "html_var": py_var })

def post_get(request):
    #Print HTTP request的方式，GET/POST
    print(request.method)

    # 在URL上傳遞value like abc.com/get_post/?page=123
    print(request.GET)

    #在Request中提交數據
    print(request.POST)

    #【Response】 HTTP-Response
    #return HttpResponse("Things to return")
    #return redirect("https://www.google.com")
    return render(request,'sth.html',{"title" : "string"})

def login(request):
    #When the User ask for the url, they will request a http GET request to get the login page
    if request.method == "GET":
        return render(request,"login.html")
    #如果是post請求獲取用戶提交的數據
    else:
        print(request.POST)
        return HttpResponse("登陸成功")
    


