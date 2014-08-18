# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from polls.models import Poll,Choice


class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_poll_list'

    def get_queryset(self):
        #print self
        #return Poll.objects.order_by('-pub_date')[:5]
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model=Poll
    template_name='polls/detail.html'
    
class ResultsView(generic.DetailView):
    model=Poll
    template_name='polls/results.html'

'''
def index(request):
    #return HttpResponse("Hello, world. You are at the poll index.")
    latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context=RequestContext(request,{
        'latest_poll_list':latest_poll_list,
        }
                           )
    return HttpResponse(template.render(context))
    #output=','.join([p.question for p in latest_poll_list])
    #return HttpResponse(output)
def detail(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/detail.html',{'poll':poll})
    #try:
    #    poll=Poll.objects.get(pk=poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    #return render(request,'polls/detail.html',{'poll':poll})
    #return HttpResponse("You are looking at the results of poll %s." % poll_id)
def results(request,poll_id):
    poll=get_object_or_404(Poll,pk=poll_id)
    return render(request,'polls/results.html',{'poll':poll})
    #return HttpResponse("You are looking at the results of pool %s." % poll_id)
    '''
def vote(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        render(request,'polls/detail.html',{
            'poll':p,
            'error_message':"You did not select a choice.",
            })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
    #return HttpResponse("You are voting on poll %s." % poll_id)


