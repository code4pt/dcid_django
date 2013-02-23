from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from parliament.models import Proposal, Tag, CreateProposalForm

def index(request):
	proposals_list = Proposal.objects.all().order_by('-timestamp')
	return render(request, 'parliament/index.html', {'proposals_list': proposals_list})

def proposals(request):
	proposals_list = Proposal.objects.all().order_by('-timestamp')
	return render(request, 'parliament/proposals.html', {'proposals_list': proposals_list})

def proposal_detail(request, proposal_id):
	proposal = get_object_or_404(Proposal, pk=proposal_id)
	return render(request, 'parliament/proposal_detail.html', {'proposal': proposal})

def proposal_create(request):
		if request.method == 'POST': # If the form has been submitted...
			form = CreateProposalForm(request.POST) # A form bound to the POST data
			if form.is_valid():
				auth_id = form.cleaned_data['username']
				title = form.cleaned_data['title']
				proposal = form.cleaned_data['proposal']
				new_prop = Proposal.objects.create_proposal(auth_id,title,proposal)
				return HttpResponseRedirect('/parliament/proposals/' + str(new_prop.id)) # Redirect after POST
			else:
				return HttpResponseRedirect('/parliament/proposal_create' + str(new_prop.id)) # Redirect after POST
		else:
			form = CreateProposalForm(auto_id=True) # An unbound form

			return render(request, 'parliament/proposal_create.html', {
				'form': form,
			})

def tags(request):
	tags_list = Tag.objects.all().order_by('name')
	return render(request, 'parliament/tags.html', {'tags_list': tags_list})

def tag_detail(request, tag_name):
	lowcase_name = tag_name.lower()
	tag = get_object_or_404(Tag, pk=lowcase_name)
	tagged_proposals = Proposal.objects.filter(tag__name = tag.name)
	return render(request, 'parliament/tag_detail.html', {'tag': tag, 'tagged_proposals': tagged_proposals})

# ========== Actions ==========
