from django.db import models
from django import forms
from datetime import datetime


class Person(models.Model):
    """
    Represents a real person capable of voting and proposing.
    """
    id_num = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    # TODO devia ser pipe
    def short_name(self):
        fullname = str(self.name)
        end_of_firstname = fullname.find(" ")
        start_of_lastname = fullname.rfind(" ") + 1
        return "{0} {1}".format(fullname[:end_of_firstname], fullname[start_of_lastname:])

    def __unicode__(self):
        return str(self.name)


class CreateProposalForm(forms.Form):
    """
    This class represents a form. This form is responsible for receiving input
    from a user in order to create a proposal.
    """
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={ 'required': 'true', 'class': 'input-xxlarge' }));
    problem = forms.CharField(label='Problem', widget=forms.Textarea(attrs={ 'required': 'true', 'rows': '3', 'class': 'input-xxlarge', 'placeholder': 'What problems needs to be solved? Use less than 300 characters.' }));
    solution = forms.CharField(label='Solution', widget=forms.Textarea(attrs={ 'required': 'true', 'rows': '3', 'class': 'input-xxlarge', 'placeholder': 'How do you suggest the problem to be solved? Use less than 300 characters.' }));
    benefits = forms.CharField(label='Benefits', widget=forms.Textarea(attrs={ 'required': 'true', 'rows': '3', 'class': 'input-xxlarge', 'placeholder': 'What are the benefits of implementing your proposal? Use less than 300 characters.' }));
    tags = forms.CharField(label='Tags', widget=forms.TextInput(attrs={ 'required': 'true', 'class': 'input-xlarge', 'placeholder': 'no-spaces, separate, by, commas' }))


class ProposalManager(models.Manager):
    """
    This class maps the input from CreateProposalForm into a Proposal object
    """
    def create_proposal(self, in_author, in_title, in_problem, in_solution, in_benefits, in_tags):
        author_obj = Person.objects.get(name = in_author)
        # TODO get the tags or create them?
        newproposal = self.create(author=author_obj, title=in_title, problem=in_problem, solution=in_solution, benefits=in_benefits, timestamp=datetime.now())
        newproposal.save()
        return newproposal


class Proposal(models.Model):
    """
    This class represents a suggestion that's started by a Person and voted
    by other Persons. A proposal is backed up by the author's arguments and
    other Persons' Opinions.
    """
    id_num = models.PositiveIntegerField(primary_key=True)
    author = models.ForeignKey(Person, related_name="author")
    title = models.CharField(max_length=70)
    problem = models.CharField(max_length=300)
    solution = models.CharField(max_length=300)
    benefits = models.CharField(max_length=300)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField()
    objects = ProposalManager()
    # TODO delete orphaned tags? http://stackoverflow.com/questions/10609699/efficiently-delete-orphaned-m2m-objects-tags-in-django

    def score(self):
        return self.upvotes - self.downvotes

    def total_votes(self):
        return self.upvotes + self.downvotes

    def set_upvotes(self, number):
        if(number >= 0):
            self.upvotes = number

    def set_downvotes(self, number):
        if(number >= 0):
            self.downvotes = number

    def __unicode__(self):
        return self.title


class ProposalVote(models.Model):
    """
    A ProposalVote stores information about votes on proposals. A Person (who)
    votes up or down (direction) a Proposal (what).
    """
    who = models.ForeignKey(Person)
    what = models.ForeignKey(Proposal)
    direction = models.BooleanField()   # true = upvote = vote in favor

    class Meta:
        unique_together = ("who", "what")   # similar to PrimaryKey, that set must be unique


class Tag(models.Model):
    """
    A Tag is a subject or theme that classifies a specimen (like a
    Proposal). Its main objective is to catalogue/group similar specimens,
    easing their search.
    """
    tagged_proposals = models.ManyToManyField(Proposal)
    name = models.CharField(primary_key=True, max_length=60)
    desc = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name


class Opinion(models.Model):
    """
    An Opinion is a long comment about something (like a Proposal) and it
    can be against or in favor. Persons other than the author can agree or
    disagree by voting up or down the Opinion.
    """
    author = models.ForeignKey(Person, related_name="opinion_author")
    proposal = models.ForeignKey(Proposal, related_name="opinion_on_proposal")
    in_favor = models.BooleanField()    # true if this oppinion is in favor of something
    text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    timestamp = models.DateTimeField()

    def score(self):
        return self.in_favor

    def __unicode__(self):
        return "{0} | {1}".format(self.text[0:20], str(self.proposal))
