from django.db import models
from django.utils import timezone #MUST ADD to use timezone
from datetime import timedelta #tdelta to use datetime
#Each model has a number of class variables, each of which represents a database field in the model.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #This tells Django what type of data each field holds.
    pub_date = models.DateTimeField('date published')

    #Change representation of Object
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
        #Added
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
       

class Choice(models.Model):
	#ForeignKey. - each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #Some Field classes have required arguments. CharField, for example, requires that you give it a max_length.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text




