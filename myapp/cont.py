from django.conf.urls import url

from . import views
app_name='myapp'
urlpatterns = [
url(r'^$',views.home,name="home"),
url(r'^(?P<rid>[0-9]+)/$',views.resturant,name="resturant"),
url(r'^rpage/(?P<mid>[0-9]+)/$',views.rmenu,name="menupage"),
url(r'^rpage/order/(?P<oid>[0-9]+)/$',views.orderpage,name="orderpage"),
url(r'^rpage/order/cart/$',views.cart,name="cartpage"),
url(r'^rpage/order/cart/(?P<cid>[0-9]+)$',views.cartdelete,name="cartdeletepage"),
url(r'^rpage/order/cart/payment$',views.payment,name="pay"),
url(r'^rpage/order/cart/payment/gateway$',views.paymentgateway,name="paygate"),
]