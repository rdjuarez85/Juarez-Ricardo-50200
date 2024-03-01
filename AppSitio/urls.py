from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name = "home"),
    path('usuario_home/', usuario_home, name = "usuario_home"),
    path('admin_home/', admin_home, name = "admin_home"),
    path('tecnico_home/', tecnico_home, name = "tecnico_home"),    
    path('nosotros/', nosotros, name = "nosotros"),
    path('contacto/', contacto, name = "contacto"),
    path('seguimiento/', seguimiento, name = "seguimiento"),
    path('seguimiento_buscar/', seguimiento_buscar, name = "seguimiento_buscar"),
    
    
    # ---------------------------------- Clientes ----------------------------------    
    path('clientes/', clientes, name = "clientes"),
    path('nuevo_cliente/', ClienteCreate.as_view(), name = "nuevo_cliente"),
    path('editar_cliente/<int:pk>/', ClienteUpdate.as_view(), name = "editar_cliente"),
    path('eliminar_cliente/<int:pk>/', ClienteDelete.as_view(), name = "eliminar_cliente"),
    path('buscar_clientes/', buscar_clientes, name = "buscar_clientes"),
    
    
    # ---------------------------------- Técnicos ----------------------------------
    path('tecnicos/', tecnicos, name = "tecnicos"),
    path('nuevo_tecnico/', TecnicoCreate.as_view(), name = "nuevo_tecnico"),
    path('editar_tecnico/<int:pk>/', TecnicoUpdate.as_view(), name = "editar_tecnico"),
    path('eliminar_tecnico/<int:pk>/', TecnicoDelete.as_view(), name = "eliminar_tecnico"),
    path('buscar_tecnicos/', buscar_tecnicos, name = "buscar_tecnicos"),
    
    
    # ---------------------------------- Trabajos ----------------------------------
    path('trabajos/', trabajos, name = "trabajos"),
    path('nuevaOT/', TrabajoCreate.as_view(), name = "nuevaOT"),
    path('editarOT/<int:pk>/', TrabajoUpdate.as_view(), name = "editarOT"),
    path('eliminarOT/<int:pk>/', TrabajoDelete.as_view(), name = "eliminarOT"),
    path('buscar_trabajos/', buscar_trabajos, name = "buscar_trabajos"),
    
    
    # ------------------------------- Compra / Venta -------------------------------
    path('publicacion/', publicacion, name = "publicacion"),
    path('nueva_publicacion/', PublicacionCreate.as_view(), name = "nueva_publicacion"),
    path('editar_publicacion/<int:pk>/', PublicacionUpdate.as_view(), name = "editar_publicacion"),
    path('eliminar_publicacion/<int:pk>/', PublicacionDelete.as_view(), name = "eliminar_publicacion"),
    path('buscar_publicaciones/', buscar_publicaciones, name = "buscar_publicaciones"),
    
    
    # --------------- Login, Logout, Registro, Editar usuario, Avatar --------------
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="AppSitio/logout.html"), name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
]