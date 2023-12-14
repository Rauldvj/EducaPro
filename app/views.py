from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages #Importamos mensajes
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required #Importamos autenticación
from django.contrib.auth.models import User 
from django.contrib.auth.models import Group
from .funciones import get_user_group_name

from .forms import * #Importamos los modelos de formularios para realizar la vista


# """ Crea vista del index """
def index(request):
    return render(request, "index.html")
#  -----------------------------------------------------------------   

#Vista para Crear un Nuevo Usuario

@login_required     
def registro(request):
    data = {
        "form": RegistroUsuarioForm()
    }
    if request.method == "POST":
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "¡Usuario Creado Correctamente!")
            return redirect(to="perfil")     
        data["form"] = formulario
    return render(request, "registration/registro.html", data)


#  -----------------------------------------------------------------   
# Crea vista para el login

def loginUser(request):
    return render(request, 'registration/login.html')
#  -----------------------------------------------------------------  
#Crea vista para el Home

def home(request):
    # Obtener el nombre del grupo para el usuario actual
    group_name = get_user_group_name(request.user)

    # Pasamos group_name al contexto si lo necesitas en tu template
    context = {'group_name': group_name}

    return render(request, 'home.html', context)
        


#  -----------------------------------------------------------------  
#Crea vista para registro de Estudiante
@login_required
def estudiante(request):
    data = {
        'form': EstudianteForm()
    }
    if request.method == 'POST':
        formulario = EstudianteForm(data=request.POST) #Recibimos la data del formulario de Estudiante
        if formulario.is_valid(): #Si el formulario es valido
            formulario.save() #Se registran los datos en la BD
            data['mensaje'] = 'Estudiante registrado' #Mensaje de éxito
        
        else:
            data['form'] = formulario #Si el formulario posee errores, este no se guardara
    return render(request, 'registro/estudiante.html', data)
    
@login_required  
def anamnesis(request):
    data = {
        'form': AnamnesisForm()
    }
    if request.method == 'POST':
        formulario = AnamnesisForm(data=request.POST) #Recibimos la data del formulario de Anamnesis
        if formulario.is_valid(): #Si el formulario es valido
            formulario.save() #Se registran los datos en la BD
            data['mensaje'] = 'Anamnesis registrado' #Tail de éxito
        
        else:
            data['form'] = formulario #Si el formulario posee errores, este no se guardara
    return render(request, 'informes/anamnesis.html', data)
        


   # VISTAS SOLO PARA LOS DIFERENTES INFORMES
@login_required
def Bitacora(request):
    return render(request, 'informes/bitacora.html') 




#  -----------------------------------------------------------------  
#Crea una Vista para el Perfil

@login_required
def edit_profile(request):
    # Obtener el usuario y el perfil asociado
    user = request.user
    profile = user.profile

    # Obtener el nombre del grupo para el usuario actual
    group_name = get_user_group_name(user)

    if request.method == 'POST':
        # Procesar el formulario si la solicitud es POST
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            # Guardar los cambios en el usuario y el perfil si ambos formularios son válidos
            user_form.save()
            profile_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado exitosamente.')
            return redirect('perfil')
        else:
            # Mostrar mensajes de error si hay problemas con los formularios
            messages.error(request, 'Error al actualizar el perfil. Verifica los errores en el formulario.')
    else:
        # Si la solicitud no es POST, inicializar los formularios con los datos actuales
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    if user.groups.first().name == 'Coordinadores':
        # Si el usuario pertenece al grupo 'Coordinadores'
        
        # Obtener todos los usuarios, grupos y perfiles para mostrar en el contexto
        all_users = User.objects.all()
        all_groups = Group.objects.all()
        user_profiles = []

        for user in all_users:
            profile = user.profile
            user_groups = user.groups.all()

            # Agregar información de cada usuario al listado
            user_profiles.append({
                'user': user,
                'groups': user_groups,
                'profile': profile
            })

        # Crear el contexto con la información recolectada
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
            'group_name': group_name,
            'user_profiles': user_profiles,
            'all_groups': all_groups,
        }

        # Renderizar la plantilla con el contexto
        return render(request, 'perfiles/perfil.html', context)
    
    return render(request, 'perfiles/perfil.html', {'user_form': user_form, 'profile_form': profile_form, 'group_name': group_name})
