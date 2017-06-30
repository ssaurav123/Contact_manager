# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from contacts.models import Contact
from .forms import PostForm




def post_new(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('contactlist')
    else:
        form = PostForm()
        return render(request, 'contacts/home.html', {'form': form})



def contact_edit(request,pk):
    ContactData = get_object_or_404(Contact,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=ContactData)
        if form.is_valid():
            ContactData=form.save()
            ContactData.save()
            return redirect('contactlist')
    else:
        form=PostForm(instance=ContactData)
    return render(request,'contacts/edit.html',{'form':form})
def contact_delete(request,pk):
    DeleteContact = get_object_or_404(Contact, pk=pk).delete()
    return redirect('contactlist')

def Contactlist(request):
    contactposts = Contact.objects.all()
    return render(request, 'contacts/contactlist.html', {'list':contactposts})