from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class Login(APIView):
    #يورث ِAPI View
    permission_classes = []
    #يعني يكدر يدز طلب على رابط بدون مايسجل يعني يكدر يدز ريكوست عادي بدون تسجيل لنو اذا حطينا IsAutch.. لازم تحط access token بي هيدارس ريكوست مالتك
    #فهذا تسجيل دخول ميحتاج access token بعد تسجيل دخول نحتاجه
    #هنا تكتب اسم داله بي اسم نوع ريكوست مثلا اذا تريده يدز get request تحط اسم داله get وهكذا
    def post(self,request) -> Response:
        try:
            username = request.data["username"]
            password = request.data["password"]
        #هنا ناخذ يوزر وباس بي داتا الي دزها مستخدم
            user = authenticate(username=username,password=password)
            #authentiact داله جاهزه منdjango تشوف يوزر وباسورد موجودين لو لا
            # اذا موجودين
            if user is not None:
                #سويله توكن
                token = RefreshToken.for_user(user)
                return Response({"data":{"message":"success","access_token":str(token.access_token),"refresh":str(token)}})
            #ورجعله توكناته
            else:
                #اذا ماموجودين كله ماكو
                return Response({"data":{"message":"username or password not found"}})
        except:
            #واذا مدز يوزر وباس بي داتا كله ايرور
            return Response({"data":{"message":"error"}})
class Created(APIView):
    permission_classes = []
    #نفس حاله سابقه مانطلب تحقق بي توكن
    def post(self,request) -> Response:
        #نوع ريكوست بوست لانو مستخدم لازم يدز داتا
        try:
            username = request.data["username"]
            password = request.data["password"]
            #ناخذ يوزر وباس الي بل داتا موجوده بل ريكوست ريكوست يعني طلب
            if User.objects.filter(username=username).exists():
                # اذا يوزر موجود بي قاعده بيانات كله يوزر مستخدم
                return Response({"data":{"Message":"username is alerdy exsist"}})
            else:
                #اذا يوزر مو موجود احفضه بي قاعد بيانات وهي تشفر باسورد تلقاةيا
                user = User.objects.create_user(username=username,password=password)
                #كله طمت عمليه بنجوحاح
                return Response({"Message":"success"})
        except:
            #واذا مدز داتا او واذا دز داتا وماكو يوزر وباس كله ايرور
            return Response({"data":{"message":"error"}})
#اول
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    #هاي يعني يطلب تحقق يعني لازم بي ريكوست الي تدزه للرابط يكون بي هيدارس access token
    def post(self,request) -> Response:
        #ريكوست من نوع بوست لانو راح ناخذ منه ريفرش توكن
        try:
            refresh_token = request.data["refresh_token"]
            #ناخذ ريفرش توكن من ريكوست داتا
            n = RefreshToken(refresh_token)
            n.blacklist()
            #ونحذفه يعني ميكدر يسوي شي بل حساب لانو بطلنا توكن مالته
            #ميكدر يستخدمه بعد
            #رجعله طمت عمليه بنجاوح
            return Response({"data":{"Message":"success"}})
        except:
            # واذا مدز ريفرش توكن كله اترو يتصل بكه
            #نروح نعرفه بي URL
            return Response({"data":{"message":"اترو يتصل بكه"}})

