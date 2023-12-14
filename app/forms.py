from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from accounts.models import *
from estudiantes.models import *

#CREAMOS EL FORMULARIO EL CUAL HEREDA LOS DATOS DEL USER
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya existe')
        return email

class ProfileForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)

    class Meta:
        model = Profile
        fields = ['image', 'rut', 'direccion', 'region', 'comuna', 'telefono']
      



#CREAMOS EL FORMULARIO EL CUAL REGISTRA Y RETORNA EN FORMATO HTML A NUESTRA VISTA DE NUEVO USUARIO

class RegistroUsuarioForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


#CREAMOS EL FORMULARIO EL CUAL REGISTRA Y RETORNA EN FORMATO HTML A NUESTRA VISTA DE ESTUDIANTE
class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'



class AnamnesisForm(forms.ModelForm):
    class Meta:
        model = Anamnesis
        fields = '__all__'
        widgets = {
            'sexo': forms.RadioSelect(attrs={'class': 'form-radio'}),
            'pediatria': forms.RadioSelect,
            'kinesiologia': forms.RadioSelect,
            'genetico': forms.RadioSelect,
            'fonoaudiologia': forms.RadioSelect,
            'neurologia': forms.RadioSelect,
            'psicologia': forms.RadioSelect,
            'psiquiatria': forms.RadioSelect,
            'psicopedagogia': forms.RadioSelect,
            'terapiaocupacional': forms.RadioSelect,
            'tipo_parto': forms.RadioSelect,
            'otro': forms.RadioSelect,
            'asistencia_medica_parto': forms.RadioSelect,
            'desnutricion': forms.RadioSelect,
            'obesidad': forms.RadioSelect,
            'fiebre_alta': forms.RadioSelect,
            'convulsiones': forms.RadioSelect,
            'traumatismos': forms.RadioSelect,
            'intoxicacion': forms.RadioSelect,
            'enfermedad_respiratoria': forms.RadioSelect,
            'asma': forms.RadioSelect,
            'encefalitis': forms.RadioSelect,
            'meningitis': forms.RadioSelect,
            'hospitalizaciones': forms.RadioSelect,
            'control_periodico_salud': forms.RadioSelect,
            'vacunas': forms.RadioSelect,
            'controla_esfinter_vesical': forms.RadioSelect,
            'controla_esfinter_anal': forms.RadioSelect,
            'actividad_motora_general': forms.RadioSelect,
            'tono_muscular_general': forms.RadioSelect,
            'estabilidad_caminar': forms.RadioSelect,
            'caida_frecuente': forms.RadioSelect,
            'dominancia_lateral': forms.RadioSelect,
            'garra': forms.RadioSelect,
            'ensarta': forms.RadioSelect,
            'presion': forms.RadioSelect,
            'dibuja': forms.RadioSelect,
            'pinza': forms.RadioSelect,
            'escribe': forms.RadioSelect,
            'reaccion_voces_caras': forms.RadioSelect,
            'demanda_obj_comp': forms.RadioSelect,
            'sonr_balb_gri_llo': forms.RadioSelect,
            'manipula_explora': forms.RadioSelect,
            'comprende_prohibiciones': forms.RadioSelect,
            'disc_ojo_mano': forms.RadioSelect,
            'estimulos_visuales': forms.RadioSelect,
            'dolores_cabeza': forms.RadioSelect,
            'ojos_irrt_llor': forms.RadioSelect,
            'acerca_aleja': forms.RadioSelect,
            'sigue_con_vista': forms.RadioSelect,
            'presenta_movimientos': forms.RadioSelect,
            'man_cond_erron': forms.RadioSelect,
            'diag_medico': forms.RadioSelect,
            'estimulo_auditivo': forms.RadioSelect,
            'voces_sonidos': forms.RadioSelect,
            'gira_cabeza': forms.RadioSelect,
            'acerca_oidos': forms.RadioSelect,
            'tapa_golpea_ojo': forms.RadioSelect,
            'dolor_oidos': forms.RadioSelect,
            'pronunciacion_oral': forms.RadioSelect,
            'otitis_hipo_otra': forms.RadioSelect,
            'nino_comunica': forms.RadioSelect,       
            'balbucea': forms.RadioSelect,
            'vocaliza': forms.RadioSelect,
            'emite_palabras': forms.RadioSelect,
            'emite_produce': forms.RadioSelect,
            'relata_expeciencias': forms.RadioSelect,
            'emision_pronunciacion': forms.RadioSelect,
            'identifica_objetos': forms.RadioSelect,
            'identifica_personas': forms.RadioSelect,
            'comprende_conceptos': forms.RadioSelect,
            'responde_coherente': forms.RadioSelect,
            'instrucciones_simples': forms.RadioSelect,
            'instrucciones_complejas': forms.RadioSelect,
            'instrucciones_grupales': forms.RadioSelect,
            'comprende_relatos': forms.RadioSelect,               
            'espontaneamente': forms.RadioSelect,
            'comportamiento_actitudes': forms.RadioSelect,
            'actividades_grupales': forms.RadioSelect,
            'trabajo_individual': forms.RadioSelect,
            'lenguaje_ecolalico': forms.RadioSelect,
            'dificultad_adaptarse': forms.RadioSelect,
            'forma_colaborativa': forms.RadioSelect,
            'normas_sociales': forms.RadioSelect,
            'normas_escolares': forms.RadioSelect,
            'sentido_humor': forms.RadioSelect,
            'movimientos_estereotipados': forms.RadioSelect,
            'pataletas_frecuentes': forms.RadioSelect,
            'luces': forms.RadioSelect,
            'sonidos': forms.RadioSelect,
            'personas_extranas': forms.RadioSelect,
            'vacunas_al_dia': forms.RadioSelect,
            'epilepsia': forms.RadioSelect,
            'problemas_cardiacos': forms.RadioSelect,
            'paraplejia': forms.RadioSelect,
            'perdida_auditiva': forms.RadioSelect,
            'perdida_visual': forms.RadioSelect,
            'trastorno_motor': forms.RadioSelect,
            'prob_bronco_resp': forms.RadioSelect,
            'enf_infect_cont': forms.RadioSelect,
            'trastorno_emocional': forms.RadioSelect,
            'trastorno_conductual': forms.RadioSelect,
            'alimentacion': forms.RadioSelect,
            'peso_apreciacion': forms.RadioSelect,
            'sueno': forms.RadioSelect,
            'duerme': forms.RadioSelect,
        }

      