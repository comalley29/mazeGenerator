from django.urls import path, include 
from mazes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.home, name='home'),
    path('styles', views.styles, name='styles'),
    path('generate', views.generate, name='generate'),
    #path('submitmaze', views.generate, name='submitmaze'),

    path('download', views.download, name='download'),
    path('<int:style_id>/', views.stylepage, name='stylepage'),

    path('aldousbroder', views.aldousbroder, name='aldousbroder'),
    path('backtracking', views.backtracking, name='backtracking'),
    path('binarytree', views.binarytree, name='binarytree'),
    path('cellularautomation', views.cellularautomation, name='cellularautomation'),
    path('dungeonrooms', views.dungeonrooms, name='dungeonrooms'),
    path('ellers', views.ellers, name='ellers'),
    path('growingtree', views.growingtree, name='growingtree'),
    path('huntandkill', views.huntandkill, name='huntandkill'),
    path('kruskals', views.kruskals, name='kruskals'),
    path('prims', views.prims, name='prims'),
    path('recursivedivision', views.recursivedivision, name='recursivedivision'),
    path('sidewinder', views.sidewinder, name='sidewinder'),
    path('wilsons', views.wilsons, name='wilsons'),

]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


