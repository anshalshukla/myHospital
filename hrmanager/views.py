from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from home.context_processors import hasGroup
from django.contrib import messages
from django.template.context_processors import csrf
from profiles.models import Doctor
from django.http import HttpResponseRedirect

# Create your views here.

# RETRIEVE
@login_required
def view(request):
    c = {}
    user = request.user
    if hasGroup(user, 'hr_manager'):
        c['isHRManager'] = True
        c['doctors'] = User.objects.filter(groups__name='doctor')
        c['receptionists'] = User.objects.filter(groups__name='receptionist')
        c['lab_attendants'] = User.objects.filter(groups__name='lab_attendant')
        c['inventory_managers'] = User.objects.filter(groups__name='inventory_manager') 

        i = 0 
        for doc in c['doctors']:
            if doc.doctor.status:
                i += 1
        c['active_doctors'] = i
    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/home')
    return render(request, 'hrmanager/view_all.html', c)

@login_required
def update_doctor_form(request, **kwargs):
    id = kwargs['id']
    user = User.objects.get(pk=id)
    c = {}
    c['doctor'] = user
    return render(request, 'hrmanager/updateDoctor.html', c)

@login_required
def update_doctor(request, **kwargs):
    id = kwargs['id']
    doc = User.objects.get(pk=id)
    user = request.user
    if hasGroup(user, 'hr_manager'):
        contact_no = request.POST.get('contact_no', '')
        gender = request.POST.get('gender', '')
        address = request.POST.get('address', '')
        blood_group = request.POST.get('blood_group', '')
        age = request.POST.get('age', '')
        outstanding = request.POST.get('outstanding', '')
        paid = request.POST.get('paid', '')
        status = request.POST.get('status', '')

        doc.doctor.contact_no = contact_no
        doc.doctor.gender = gender
        doc.doctor.address = address
        doc.doctor.blood_group = blood_group
        doc.doctor.age = age
        doc.doctor.outstanding = outstanding
        doc.doctor.paid = paid
        doc.doctor.status = status
        doc.doctor.save()        

        messages.add_message(request, messages.INFO, 'Profile successfully updated!')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.WARNING, 'Access Denied.')
        return HttpResponseRedirect('/') 

@login_required
def delete_doctor(request, **kwargs):
    user = request.user
    if hasGroup(user, 'hr_manager'):
        id = kwargs['id']
        User.objects.get(pk=id).delete()
        messages.add_message(request, messages.INFO, 'Doctor has been successfully deleted!')
        return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.WARNING, 'Access denied!')
        return HttpResponseRedirect('/')