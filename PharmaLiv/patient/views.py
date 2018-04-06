from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from .forms import signUp,FemmeForm
from patient.models import Ordonnances,Patient
# Create your views here.
def reponse(request):
    Patient.objects.filter(user_id=request.user.id).update(id=request.user.id),  
    context = {
        'notifications':Ordonnances.objects.filter(patient_id=request.user.id).filter(notifications='non lu').count(),
        'messages':Ordonnances.objects.filter(patient_id=request.user.id).filter(notifications='non lu'),
        'ordo':Ordonnances.objects.filter(patient_id=request.user.id).order_by('-dateSoumission'), 
        'patien':Patient.objects.get(id=request.user.id),  
    }
    return render(request,'patient/reponse.html',context)


class reponseFemme(FormView):
    template_name="patient/etat.html"
    form_class = FemmeForm
    success_url ='/patient/thanks/'
    
    def form_valid(self,form):
        form.save()
        return super(reponseFemme, self).form_valid(form)

def home(request):
    return render(request,'patient/home.html')

def notification(request):
    context = {
        'messages':Ordonnances.objects.filter(patient_id=request.user.id) 
    } 
    Ordonnances.objects.filter(patient_id=request.user.id).update(notifications='lu')
    return render(request,'patient/messages.html',context)

class connexionView(FormView):
    template_name="patient/newForm.html" #juste pour tester le formulaire de materialize bootstrap
    form_class = signUp
    success_url ='/patient/thanks/'

    def form_valid(self,form):
        """This method is called when valid form data has been POSTed.
        It should return an HttpResponse."""
        user= form.save()
        login(self.request,user)
        return super().form_valid(form)