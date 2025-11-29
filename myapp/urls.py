from django.urls import path

from myapp.views import analysis, default, home, save_analysis
# from imsdLearn.view import analysis, home, default
# from . import views

urlpatterns = [
    # path('', index, name='myapp_index'),
    # path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', default, name='default'),
    path('analysis/', analysis, name='analysis'),
    path('save_analysis/', save_analysis, name='save_analysis'),
]
