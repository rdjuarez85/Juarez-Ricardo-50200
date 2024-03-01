from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *
from django.db.models import Q

from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



# Create your views here.

def es_admin(user):                                                 # Funcion para definir si pertenece al grupo Admins
    return user.groups.filter(name='Admins').exists()


class AdminRequiredMixin(LoginRequiredMixin):                       # Para verificar si es admin
    def dispatch(self, request, *args, **kwargs):
        if not es_admin(request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


def es_tecnico(user):                                               # Funcion para definir si pertenece al grupo Tecnicos
    return user.groups.filter(name='Tecnicos').exists()
    

def es_admin_o_tecnico(user):                                       # Funcion para definir si pertenece a cualquiera de los grupos Admins o Tecnicos
    return user.groups.filter(name='Admins').exists() or user.groups.filter(name='Tecnicos').exists()


class AdminOrTecnicoRequiredMixin(UserPassesTestMixin):             # Para verificar si es admin o tecnico
    def test_func(self):
        user = self.request.user
        return user.groups.filter(name='Admins').exists() or user.groups.filter(name='Tecnicos').exists()


# ------------------------------------ Home ------------------------------------
def home(request):
    if request.user.is_authenticated:
        if es_admin(request.user):
            return redirect('admin_home')                           # Si pertenece al grupo Admins
        elif es_tecnico(request.user):
            return redirect('tecnico_home')                         # Si pertenece al grupo Tecnicos
        else:
            return redirect('usuario_home')                         # Si es un usuario común
    else:
        return render(request, "AppSitio/home.html")                # Si no esta logueado


@login_required
@user_passes_test(es_admin)
def admin_home(request):
    return render(request, "AppSitio/admin_home.html")


@login_required
@user_passes_test(es_admin_o_tecnico)
def tecnico_home(request):
    return render(request, "AppSitio/tecnico_home.html")


@login_required
def usuario_home(request):
    return render(request, "AppSitio/usuario_home.html")


# ---------------------------------- Clientes ----------------------------------
@login_required
@user_passes_test(es_admin)
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "AppSitio/clientes.html", contexto)


class ClienteCreate(AdminRequiredMixin, CreateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')


class ClienteUpdate(AdminRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('clientes')


class ClienteDelete(AdminRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes')


@login_required
@user_passes_test(es_admin)
def buscar_clientes(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        clientes = Cliente.objects.filter(Q(nombre__icontains=patron) | Q(apellido__icontains=patron))
        contexto = {"clientes": clientes}
        return render(request, "AppSitio/clientes.html", contexto)


# ---------------------------------- Técnicos ----------------------------------
@login_required
@user_passes_test(es_admin)
def tecnicos(request):
    contexto = {'tecnicos': Tecnico.objects.all()}
    return render(request, "AppSitio/tecnicos.html", contexto)


class TecnicoCreate(AdminRequiredMixin, CreateView):
    model = Tecnico
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('tecnicos')


class TecnicoUpdate(AdminRequiredMixin, UpdateView):
    model = Tecnico
    fields = ['nombre', 'apellido', 'email']
    success_url = reverse_lazy('tecnicos')


class TecnicoDelete(AdminRequiredMixin, DeleteView):
    model = Tecnico
    success_url = reverse_lazy('tecnicos')


@login_required
@user_passes_test(es_admin)
def buscar_tecnicos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        tecnicos = Tecnico.objects.filter(Q(nombre__icontains=patron) | Q(apellido__icontains=patron))
        contexto = {"tecnicos": tecnicos}
        return render(request, "AppSitio/tecnicos.html", contexto)


# ---------------------------------- Trabajos ----------------------------------
@login_required
@user_passes_test(es_admin_o_tecnico)
def trabajos(request):
    contexto = {'trabajos': Trabajo.objects.all()}
    return render(request, "AppSitio/trabajos.html", contexto)


class TrabajoCreate(LoginRequiredMixin, AdminOrTecnicoRequiredMixin, CreateView):
    model = Trabajo
    fields = ['dispositivo', 'falla', 'observaciones']
    success_url = reverse_lazy('trabajos')


class TrabajoUpdate(LoginRequiredMixin, AdminOrTecnicoRequiredMixin, UpdateView):
    model = Trabajo
    fields = ['dispositivo', 'falla', 'observaciones', 'estado']
    success_url = reverse_lazy('trabajos')


class TrabajoDelete(LoginRequiredMixin, AdminOrTecnicoRequiredMixin, DeleteView):
    model = Trabajo
    success_url = reverse_lazy('trabajos')
    

@login_required
@user_passes_test(es_admin_o_tecnico)
def buscar_trabajos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        trabajos = Trabajo.objects.filter(ot_nro__icontains=patron)
        contexto = {"trabajos": trabajos}
        return render(request, "AppSitio/trabajos.html", contexto)
    

# ------------------------------- Publicaciones --------------------------------
@login_required
def publicacion(request):
    contexto = {'publicacion': Publicacion.objects.all()}
    contexto['si_es_admin'] = request.user.groups.filter(name='Admins').exists()
    return render(request, "AppSitio/publicacion.html", contexto)


class PublicacionCreate(LoginRequiredMixin, CreateView):
    model = Publicacion
    fields = ['producto', 'descripcion', 'condicion', 'precio', 'vendedor', 'email']
    success_url = reverse_lazy('publicacion')


class PublicacionUpdate(AdminRequiredMixin, UpdateView):
    model = Publicacion
    fields = ['producto', 'descripcion', 'condicion', 'precio', 'vendedor', 'email']
    success_url = reverse_lazy('publicacion')


class PublicacionDelete(AdminRequiredMixin, DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicacion')


@login_required    
def buscar_publicaciones(request):
    if "buscar" in request.GET:
        patron = request.GET["buscar"]
        publicaciones = Publicacion.objects.filter(producto__icontains=patron)
        contexto = {
            'publicacion': publicaciones,
            'si_es_admin': request.user.groups.filter(name='Admins').exists()
        }
        return render(request, "AppSitio/publicacion.html", contexto)


# --------------- Login, Logout, Registro, Editar usuario, Avatar --------------
def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)            
            
            # ------Avatar------
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            # ------------------                
                
            if user.groups.filter(name='Admins').exists():
                return redirect('admin_home')
            elif user.groups.filter(name='Tecnicos').exists():
                return redirect('tecnico_home')
            else:
                return redirect('usuario_home')
        else:
            return redirect('login')
    else:
        miForm = AuthenticationForm()
        return render(request, "AppSitio/login.html", {"form": miForm })    


def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('usuario_home'))

    else:    
        miForm = RegistroForm()

    return render(request, "AppSitio/registro.html", {"form": miForm })


@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            update_session_auth_hash(request, user)
            if user.groups.filter(name='Admins').exists():
                return redirect('admin_home')
            elif user.groups.filter(name='Tecnicos').exists():
                return redirect('tecnico_home')
            else:
                return redirect('usuario_home')
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "AppSitio/editar_perfil.html", {"form": form }) 


@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ---------- Borrar avatar viejo ----------
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # -----------------------------------------
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ------ Url en la imagen en request ------
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "AppSitio/home.html")
            # -----------------------------------------

    else:    
        form = AvatarForm()

    return render(request, "AppSitio/agregar_avatar.html", {"form": form })


# -------------------------------- Otras vistas --------------------------------
def nosotros(request):
    return render(request, "AppSitio/nosotros.html")


def contacto(request):
    return render(request, "AppSitio/contacto.html")


@login_required
def seguimiento(request):
    return render(request, "AppSitio/seguimiento.html")


@login_required
def seguimiento_buscar(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        trabajos = Trabajo.objects.filter(ot_nro__icontains=patron)
        contexto = {"trabajos": trabajos}
        return render(request, "AppSitio/seguimiento_buscar.html", contexto)