from parliament.models import Proposal, Tag, CreateProposalForm, ProposalVote, Person
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf


def index(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    return render(request, 'parliament/index.html')


def proposals(request):
    proposals_list = Proposal.objects.all().order_by('-timestamp')
    return render(request, 'parliament/proposals.html', {'proposals_list': proposals_list})


def proposal_detail(request, proposal_id):
    proposal = get_object_or_404(Proposal, pk=proposal_id)
    return render(request, 'parliament/proposal_detail.html', {'proposal': proposal})


def proposal_create(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = CreateProposalForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            in_author = 'someone anonymous'  # TODO get_or_404(person)
            in_title = form.cleaned_data['title']
            in_problem = form.cleaned_data['problem']
            in_solution = form.cleaned_data['solution']
            in_benefits = form.cleaned_data['benefits']
            in_tags = form.cleaned_data['tags']
            new_prop = Proposal.objects.create_proposal(in_author, in_title, in_problem, in_solution, in_benefits, in_tags)
            return HttpResponseRedirect('/parliament/proposals/' + str(new_prop.id_num))  # Redirect after POST
        else:
            return HttpResponseRedirect('/parliament/proposal_create' + str(new_prop.id_num))  # Redirect after POST
    else:
        form = CreateProposalForm(auto_id=True)  # An unbound form
        return render(request, 'parliament/proposal_create.html', {'form': form})


def tags(request):
    tags_list = Tag.objects.all().order_by('name')
    return render(request, 'parliament/tags.html', {'tags_list': tags_list})


def tag_detail(request, tag_name):
    lowcase_name = tag_name.lower()
    tag = get_object_or_404(Tag, pk=lowcase_name)
    tagged_proposals = Proposal.objects.filter(tag__name=tag.name)
    return render(request, 'parliament/tag_detail.html', {'tag': tag, 'tagged_proposals': tagged_proposals})


# ========== Authentication ==========


def login(request):
    """
    Sends a visitor to the login page.
    """
    c = {}
    c.update(csrf(request))
    return render(request, 'parliament/login.html', c)


def auth_view(request):
    """
    Verifies if the user really exists, and if so logs in.
    """
    username = request.POST.get('form_username', '')  # '' is a fool proof
    password = request.POST.get('form_password', '')
    user = auth.authenticate(username=username, password=password)  # returns a User if it exists, None otherwise
    if user is not None:
        auth.login(request, user)  # User exists, thus log him or her in
        return HttpResponseRedirect('/parliament/user/login/success/')
    else:
        return HttpResponseRedirect('/parliament/user/login/invalid/')


def login_success(request):
    """
    Shows a login success message.
    """
    return render(request, 'parliament/login_success.html', {'username': request.user.username})


def login_invalid(request):
    """
    Shows a login insuccess message.
    """
    return render(request, 'parliament/login_invalid.html')


def logout(request):
    """
    Logs user out.
    """
    auth.logout(request)
    return HttpResponseRedirect('/parliament/user/logout/')


# ========== Registration ==========


def register(request):
    """
    TODO
    """
    is_error = False
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/parliament/user/register/success')
        else:
            is_error = True  # the form is not valid 
    args = {}
    args.update(csrf(request))    
    args['form'] = UserCreationForm()
    args['error'] = is_error
    return render(request, 'parliament/register.html', args)


def register_success(request):
    """
    Shows a success page after registering a user.
    """
    return render(request, 'parliament/register_success.html')


# ========== Actions ==========


def proposal_vote(request, proposal_id, vote_direction):
    proposal = get_object_or_404(Proposal, pk=proposal_id)
    voter = Person.objects.get(id_num=5555)  # TODO use login module
    first_time_voting = (ProposalVote.objects.filter(who=voter, what=proposal).count() == 0)
    if first_time_voting:
        # cast the vote
        is_upvote = True if vote_direction == "up" else False
        new_vote = ProposalVote.objects.create(who=voter, what=proposal, direction=is_upvote)
        new_vote.save()
        # update the number of votes
        new_number = ProposalVote.objects.filter(what=proposal, direction=is_upvote).count()
        if is_upvote:
            proposal.upvotes = new_number
        else:
            proposal.downvotes = new_number
        # end voting
        proposal.save()
        message = 'Voted successfully.'
    else:
        message = "You can't vote twice on the same proposal."
    return render(request, 'parliament/proposal_detail.html', {'proposal': proposal, 'message': message})
