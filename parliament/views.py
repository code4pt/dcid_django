from django.template import RequestContext
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from parliament.models import Proposal, Tag, CreateProposalForm

def proposals(request):
	proposals_list = Proposal.objects.all().order_by('-timestamp')
	return render(request, 'parliament/proposals.html', {'proposals_list': proposals_list})

def proposal_detail(request, proposal_id):
	proposal = get_object_or_404(Proposal, pk=proposal_id)
	return render(request, 'parliament/proposal_detail.html', {'proposal': proposal}, context_instance=RequestContext(request))

def proposal_create(request):
		if request.method == 'POST': # If the form has been submitted...
			form = CreateProposalForm(request.POST) # A form bound to the POST data
			if form.is_valid():
				auth_id = 'someone anonymous' # TODO get_or_404(person)
				title = form.cleaned_data['title']
				description = form.cleaned_data['description']
				benefits = form.cleaned_data['benefits']
				tags = form.cleaned_data['tags']
				new_prop = Proposal.objects.create_proposal(auth_id, title, description, benefits, tags)
				return HttpResponseRedirect('/parliament/proposals/' + str(new_prop.id)) # Redirect after POST
			else:
				return HttpResponseRedirect('/parliament/proposal_create' + str(new_prop.id)) # Redirect after POST
		else:
			form = CreateProposalForm(auto_id=True) # An unbound form

			return render(request, 'parliament/proposal_create.html', {
				'form': form,
			})

def proposal_create_finish(request):
	# try:
		# title = request.POST['title']
		# desc = request.POST['desc']
	# except (KeyError):
		# # Redisplay the poll voting form.
		# return render_to_response('parliament/proposal_create.html', {
			# 'error_message': "Please fill out all fields.",
			# }, context_instance=RequestContext(request))
	# new_prop = Proposal.objects().insert(title, desc)
	# Proposal.objects().save
	# Always return an HttpResponseRedirect after successfully dealing
	# with POST data. This prevents data from being posted twice if a
	# user hits the Back button.
	#return HttpResponseRedirect(reverse('parliament.views.proposal_detail', args=1
	return
	
def tags(request):
	tags_list = Tag.objects.all().order_by('name')
	return render(request, 'parliament/tags.html', {'tags_list': tags_list})

def tag_detail(request, tag_name):
	lowcase_name = tag_name.lower()
	tag = get_object_or_404(Tag, pk=lowcase_name)
	tagged_proposals = Proposal.objects.filter(tag__name = tag.name)
	return render(request, 'parliament/tag_detail.html', {'tag': tag, 'tagged_proposals': tagged_proposals})

def index(request):
    proposals_list = Proposal.objects.all().order_by('-timestamp')
    return render(request, 'parliament/index.html', {'proposals_list': proposals_list})
