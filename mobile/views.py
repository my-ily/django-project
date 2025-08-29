from django.shortcuts import render ,get_object_or_404, redirect 
from django.http import HttpResponse ,JsonResponse
from django.template import loader
from .models import Category
from .models import Product ,Cart
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login
# Create your views here.
#backend
def Welcome(request):
    return HttpResponse("hello")

def getdata(request):
    data={
        'name':'ahmed',
        'age':25,
        'skill':['py','js']
    }
    return JsonResponse(data)


def datasend(request,name):
 return HttpResponse(name)


def add(request ,x,y):
   return HttpResponse(x+y)

def invoice(request):
    if request.method == "POST":
        phone_id = request.POST.get("phone_id")
        full_name = request.POST.get("full_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        phones_list = [
            {
                "id": "0001",
                "name": "iPhone 15",
                "brand": "Apple",
                "price": 4555,
                "color": "black",
                "image": "/images/iphone15.jpg"
            },
            {
                "id": "0002",
                "name": "Samsung Galaxy S23",
                "brand": "Samsung",
                "price": 3999,
                "color": "blue",
                "image": "/images/galaxy_s24.jpg"
            },
            {
                "id": "0003",
                "name": "Samsung Galaxy r23",
                "brand": "Samsung",
                "price": 3999,
                "color": "blue",
                "image": "/images/galaxy_s24.jpg"
            }
        ]

        selected_product = [p for p in phones_list if str(p["id"]) == str(phone_id)]

        return render(request, 'invoice.html', {
            "full_name": full_name,
            "phone": phone,
            "email": email,
            "product": selected_product
        })

    return HttpResponse("This page only supports POST method.", status=405)

    

def runindex(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def landpage(request):
   #SELECT * FROM Category
   category = Category.objects.all()
   context ={
      'data':category
   }
   return render(request,'landpage.html',context)

#    template=loader.get_template('landpage.html')
#    return HttpResponse(template.render())

def about(request):
   template =loader.get_template('about.html')
   return HttpResponse(template.render())


def blog(request):
   template =loader.get_template('blog.html')
   return HttpResponse(template.render())


def phonemenu(request):
    #get prameter value  send from user
    #أنت تطلب عرض تفاصيل منتج محدد. هذه العملية تعتبر قراءة فقط، لذلك GET هي الأنسب.
    # الان راح تكون ارقام مابين ١ ٢ ٣ لانها صارت خاصه في الcategry
    phone_id = request.GET.get("id")
    # الي عندهم نفس رقم 
    # id Category 
    # هم بس الي نضافون
    product = Product.objects.filter(category_id=phone_id)
    context = {
        'product': product
    }

    return render(request,'phonemenu.html',context)
  


def morning(request):
   names=[
      {
         "name":"ah",
         "age":22 ,
         "dream":"unlimit"
      }
   ]
   context={
      'names':names
   }
#    template=loader.get_template('morning.html')
   return render(request,'morning.html',context)

def Datils(request):
   id =request.GET.get("id")
   #استخدام الـ id للبحث في قاعدة البيانات
   product = Product.objects.filter(id=id)
   context ={
      'product':product
   }
   return render(request,'details.html',context)

#if item is in cart => created =false + q=1
#if item not in cart =>craeted = true + q+1
def add_to_cart(request):
    product_id =request.GET.get("id")
   #  count = Product.objects.filter(id=id)
    cart_item , created =Cart.objects.get_or_create(
       product_id=product_id ,
       defaults={'quntity':1}

    )
   
    if not created:
     cart_item.quntity +=1
     cart_item.save()
    product = Product.objects.filter(id=product_id)
    context ={
      'product':product
    }
    return render(request,'details.html',context)

from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth_login")
def Checkout(request):
    print(f"User authenticated? {request.user.is_authenticated}")
    cart = Cart.objects.select_related("product").all()
    context = {
        'cart': cart
    }
    return render(request, 'Checkout.html', context)




def auth_login(request):
   if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    #للتحقق مما إذا كانت معلومات المستخدم صحيحة (موجودة في قاعدة البيانات، وكلمة المرور صحيحة).
    user=authenticate(request,username=username ,password=password )


    if user is not None:
       login(request,user)
#نقل المستخدم إلى صفحة ثانية (بعد تنفيذ حدث مثل تسجيل دخول
       return redirect("Checkout")
    
   return render(request,'auth/auth_login.html')  
   #  template =loader.get_template('auth/auth_login.html')
   #  return HttpResponse(template.render())




@csrf_exempt
def auth_reg(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # نحفظ المستخدم
            print("✅ النموذج صالح، جاري إنشاء المستخدم")
            login(request, user)  # نسجل دخوله مباشرة
            return redirect('Checkout')  # نوديه على صفحة الدفع مباشرة مثلاً
        else:
            print("❌ النموذج غير صالح")
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'auth/auth_reg.html', {'form': form})
   #  return HttpResponse(template.render())



























# def Checkout(request):
#    cart = Cart.objects.all()
#    context={
#       'cart':cart
#    }
#    return render(request,'Checkout.html',context)

   # template=loader.get_template("checkout.html")
   # return HttpResponse(template.render())






   #phonemeny

    # phone = [
    #     {
    #          "id":"0001",
    #         "name": "iPhone 15",
    #         "brand": "Apple",
    #         "price": 4555,
    #         "color": "black",
    #         "image":"/images/iphone15.jpg"
    #     },
    #     {
    #          "id":"0002",
    #         "name": "Samsung Galaxy S23",
    #         "brand": "Samsung",
    #         "price": 3999,
    #         "color": "blue",
    #         "image":"/images/galaxy_s24.jpg"
    #     },
    #     {
    #        "id":"0003",
    #         "name": "Samsung cover r23",
    #         "brand": "Samsung",
    #         "price": 3999,
    #         "color": "blue",
    #         "image":"/images/galaxy_s24.jpg"
    #     }
    # ]


    # template = loader.get_template('phonemenu.html')
    #translate to collection
    #request is function data
    #click button
    # if phone_id:
    #    #for loop
    #    #one item object
    #    phones=[p for p in phone if str(p["id"]) == str(phone_id)]
    #    context={"phone":phone}
    #    print(phones)
    #    return render(request, 'details.html',{"phone":phones ,"phone_id":phone_id})
      # return HttpResponse(template.render(context, request))