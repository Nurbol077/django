from django.shortcuts import render,redirect
from account.models import User


def register(request):
    if request.method =='POST':
        try:
            User.objects.create_user(
                email=request.POST['email'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
            )
        except User.DoesNotExist:
            return redirect('register')
    return render(request,'account/register_login.html')

# def create_person(request):
#     if request.method == "GET":
#         data = request.GET
#         print(data.get('email', 'example@gail.com'))
#         print(data.get('password','example'))
#         try:
#             user = User.objects.create_user(
#             email=data.get('email','example@gmail.com'),
#             password = data.get('password', 'example'),
#             first_name = data.get('first_name','example'),
#             last_name = data.get('last_name','example')
#             )
#         except Exception:
#             return HttpResponse("С такой почтой пользователь уже существует!")
#
#     return HttpResponse(f'{user.email} с такой почтой создан новый пользователь')
#
#
# def create_user(request):
#     if request.method == "POST":
#         first_name = request.POST.get('first_name','jok')
#         last_name = request.POST.get('last_name','jok')
#         email = request.POST.get('email','jok')
#         password = request.POST.get('password','jok')
#
#         try:
#             User.objects.create_user(
#                 email=email,
#                 password=password,
#                 first_name=first_name,
#                 last_name=last_name
#             )
#         except User.DoesnotExist:
#             return Http404("Такой пользователь уже существует")
#
#         return HttpResponse("Success")
#     return render(request,'account/create_user.html')
