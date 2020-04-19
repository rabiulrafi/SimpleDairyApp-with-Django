from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    entries= Entry.objects.order_by('-date_posted')
    context={
        "entries":entries
    }

    return render(request,'entries/index.html',context)
def add(request):
    if request.method=='POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryForm()

    context= {'form': form}
    return render(request,'entries/add.html',context)


def delete_Entry(request, id):

    entry_to_delete = Entry.objects.get(id=id)  
    print(entry_to_delete)
    entry_to_delete.delete()
 
    return redirect('home')
