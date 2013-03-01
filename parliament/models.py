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
	This class represents a form. This form is responsible for receiving input~
	from a user in order to create a proposal.
	"""
	title = forms.CharField(label='Title', widget=forms.TextInput(attrs={ 'required': 'true', 'class': 'input-xxlarge' }));
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={ 'required': 'true', 'rows': '4', 'class': 'input-xxlarge', 'placeholder': 'describe it in less than XX characters' }));
	benefits = forms.CharField(label='Motivation / Benefits', widget=forms.Textarea(attrs={ 'required': 'true', 'rows': '4', 'class': 'input-xxlarge', 'placeholder': 'What are the benefits of implementing your proposal?' }))
	tags = forms.CharField(label='Tags', widget=forms.TextInput(attrs={ 'required': 'true', 'class': 'input-xlarge', 'placeholder': 'no-spaces, separate, by, commas' }))


class ProposalManager(models.Manager):
	"""
	This class maps the input from CreateProposalForm into a Proposal object
	"""
	def create_proposal(self, auth_name, title, description, benefits, tags):
		author_obj = Person.objects.get(name = auth_name)
		# TODO get the tags or create them?
		newproposal = self.create(author=author_obj, title=title, desc=description, reasons=benefits, timestamp=datetime.now())
		newproposal.save()
		return newproposal


class Proposal(models.Model):
	"""
	This class represents a suggestion that's started by a Person and voted
	by others. A proposal is backed up by the author's arguments and debated
	through other Persons' Opinions.
	"""
	author = models.ForeignKey(Person, related_name="author")
	title = models.CharField(max_length=70)
	desc = models.CharField(max_length=300)
	reasons = models.CharField(max_length=300)
	upvotes = models.PositiveIntegerField(default=0)
	downvotes = models.PositiveIntegerField(default=0)
	views = models.PositiveIntegerField(default=0)
	timestamp = models.DateTimeField()
	objects = ProposalManager()
	# TODO delete orphaned tags! http://stackoverflow.com/questions/10609699/efficiently-delete-orphaned-m2m-objects-tags-in-django
	
	def score(self):
		return self.upvotes - self.downvotes
	
	def total_votes(self):
		return self.upvotes + self.downvotes
		
	def voteup(self):
		self.upvotes += 1
	
	def votedown(self):
		self.downvotes += 1
				
	def __unicode__(self):
		return self.title


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
	can be against or in favor. Persons	other than the author can agree or
	disagree by voting up or down the Opinion.
	"""
	author = models.ForeignKey(Person, related_name="opinion_author")
	proposal = models.ForeignKey(Proposal, related_name="opinion_on_proposal")
	in_favor = models.BooleanField()	#true if this oppinion is in favor of something
	text = models.CharField(max_length=200)
	score = models.IntegerField(default=0)
	timestamp = models.DateTimeField()
	
	def score(self):
		return self.in_favor
	
	def __unicode__(self):
		return "{0} | {1}".format(self.text[0:20], str(self.proposal))

