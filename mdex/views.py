from django.shortcuts import  render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from markdownex.mdex.forms import MdForm

def index(request):
     return HttpResponseRedirect('/md/')

def mdForm(request):
    if request.method == 'POST':
        form = MdForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            return render_to_response('mdex/render.html',{'mdBody': cd['markdown'],}, context_instance=RequestContext(request))
    else:
        form = MdForm(
            initial={'author': 'Me'}
        )
    return render_to_response('mdex/md_form.html', {'form': form}, context_instance=RequestContext(request))

