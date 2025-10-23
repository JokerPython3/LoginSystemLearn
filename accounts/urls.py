from django.urls import path
from rest_framework_simplejwt.views import (
TokenObtainPairView, #يولد توكن من تدزله يوزر وباس بدون متروح لي تسجيل دخول
TokenRefreshView, #يعمل تحديث للتوكن
TokenVerifyView, # يتحقق من توكن
)
from .views import Login, Created, Logout

urlpatterns = [
    path("api/token/app/",TokenObtainPairView.as_view(),name="Token"),
    path("api/token/refresh/",TokenVerifyView.as_view(),name="To"),
    path("api/token/verify/",TokenVerifyView.as_view(),name="Token"),
    path("api/login/",Login.as_view(),name="Login"),
    path("api/created/account/",Created.as_view(),name="ntro"),
    path("api/account/auth/logout/",Logout.as_view(),name="Logout")
#خنسوي ميكرشن حتى يحفض كلشي بي داتا بيس
    #نعرفه
    #شتغل خلنشغل
]