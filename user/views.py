from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse
from .models import user as user_detail

#user_follow
def follow_view(request,follower,followed):

	str = "Follower : " + follower + "<br>" + "Followed : " + followed

	user = user_detail.objects.get(pk=follower)

	user.following.append(followed)

	user_followed = user_detail.objects.get(pk=followed)

	user_followed.follower.append(user.usernameid)

	user.save()
	user_followed.save()
	

	
 
	return redirect('search:main')



#user_follow
def unfollow_view(request,unfollower,unfollowed):
	
	str = "Unfollower : " + unfollower + "<br>" + "Unfollowed : " + unfollowed


	user = user_detail.objects.get(pk=unfollower)

	user.following.remove(unfollowed)

	user_followed = user_detail.objects.get(pk=unfollowed)

	user_followed.follower.append(user.usernameid)


	user.save()
	user_followed.save()

	
	return redirect('search:main')





# user tag associater
def associateTag_view(request,name,tag):

	username =name

	user = user_detail.objects.get(username = username )

	user.tags.append(tag)

	user.save()

	str = user.username + user.address + '<br>' + user.tags[0] + user.tags[1] + '$$$' + name

	return HttpResponse(str)


# Create your views here.
def registration_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('feed:render')
			# lead to extra detail addition or verification
	else:
		form = UserCreationForm()

	return render(request,'regist.html',{'form':form})


def login_view(request):
	if request.method == 'POST' :
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)

			return redirect('feed:render')

			# redirect to source page 
			# may be not needed if kept at on first place
			# or design a closed app

	else:
		form = AuthenticationForm()
	return render(request,'login.html',{'form':form})

# logout a user
def logout_view(request):
	logout(request)
	return redirect('feed:render')


# shows the choice page
def choice_view(request):
	return render(request,'choice.html')

# create user details
def userDetail_view(request):
	user = request.user.username
	if request.method == 'POST':
		detail_form = forms.CreateUserDetail(request.POST,request.FILES)
		if detail_form.is_valid():
			instance = detail_form.save()
			return redirect('feed:render')

	else:
		detail_form = forms.CreateUserDetail()
	return render(request,'userDetail.html',{'form':detail_form,'user':user})