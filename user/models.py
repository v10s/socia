from django.db import models
from multiselectfield import MultiSelectField
from django_countries.fields import CountryField
from django_mysql.models import ListCharField

sex_choices =(('Male','Male'),('Female','Female'),('Other','Other'),('Rather not ask','rather not ask'))



# Create your models here.
class user(models.Model):

	#userid = models.AutoField(default=0,primary_key=True)
	username = models.CharField(max_length=25)
	usernameid = models.SlugField(default='',max_length=25,unique=True,blank=False,primary_key=True)

	#asssociaters
	follower = ListCharField(base_field=models.CharField(max_length=50),size=10000,max_length=(100000*50))
	following = ListCharField(base_field=models.CharField(max_length=50),size=10000,max_length=(100000*50))

	DOB = models.DateField(blank=False)
	sex = models.CharField(max_length=25,choices=sex_choices)
	tags = MultiSelectField(default='',editable=False)
	country = CountryField(default='')
	
	emailId = models.EmailField(max_length=64,unique=True,blank=False)
	profile_pic = models.ImageField(blank=False,upload_to='proupload/%Y/%m/%d/')
	


def __str__(self):
	return (self.username)



