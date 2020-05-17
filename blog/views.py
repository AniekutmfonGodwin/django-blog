from django.shortcuts import render,redirect
from .models import Post,Profile,Comment
from .utility import _all_post_tag,_hashtag,_unique_list
from .forms import CommentForm
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime





# Create your views here.

def home(request):
    
    qs=Post.objects.all().order_by('pub_date')
    print('position:',1)
    if request.user.is_authenticated:
        context = {
        'profile':Profile.objects.get(user=request.user),
        'posts':qs,
        'tags':_all_post_tag(model=Post.objects.all()),
        'categories':[c[0].title() for c in Post.CATEGORY],
        'slides':Post.objects.all().order_by('-pk')[:3],
        'top':Post.objects.all().order_by('pk')[:3],
        'lifestyle_post':Post.objects.filter(category='Lifestyle').order_by('pub_date'),
        'more_blog_post':Post.objects.all().order_by('pk')[:10],
        #not morethan 3
        'popular_post':'',
        'latest_post':Post.objects.all().order_by('-pk')[:20],
        'locations':_unique_list([c.location.title() for c in Post.objects.all()]),
        }
    else:
        context = {
        # 'profile':Profile.objects.get(user=request.user),
        'posts':qs,
        'tags':_all_post_tag(model=Post.objects.all()),
        'categories':[c[0].title() for c in Post.CATEGORY],
        'slides':Post.objects.all().order_by('-pk')[:3],
        'top':Post.objects.all().order_by('pk')[:3],
        'lifestyle_post':Post.objects.filter(category='Lifestyle').order_by('pub_date'),
        'more_blog_post':Post.objects.all().order_by('pk')[:10],
        #not morethan 3
        'popular_post':'',
        'latest_post':Post.objects.all().order_by('-pk')[:20],
        'locations':_unique_list([c.location.title() for c in Post.objects.all()]),
        }

    print('position:',2)
    return render(request, 'blog/index.html', context)


def contact(request):
    context = {
        
    }
    return render(request, 'contact.html', context)
    

    
def list_view(request,list_tag=''):
    list_type=request.GET.get('list_type','category')
    if list_type == 'category':
        qs = Post.objects.filter(category__icontains=list_tag)
    elif list_type == 'tag':
        qs = Post.objects.filter(tags__icontains=list_tag)
    elif list_type == 'location':
        qs = Post.objects.filter(location__icontains=list_tag)
    else:
        qs = Post.objects.all()

    context = {
        'list_tag': list_tag,
        'list_type': list_type.title(),
        'profile':Profile.objects.get(user=request.user),
        'queries':qs,
        'tags':_all_post_tag(model=Post.objects.all()),
        'categories':[c[0].title() for c in Post.CATEGORY],
        'lifestyle_post':Post.objects.filter(category='Lifestyle').order_by('pub_date'),
        #not morethan 3
        'popular_post':'',
        'latest_post':Post.objects.all().order_by('-pk')[:20],
        'locations':_unique_list([c.location.title() for c in Post.objects.all()]),
       


    }
    return render(request, 'blog/category.html', context)


def blog_single(request,slug=None,id=''):
    print('position:',3)
    if request.method=='GET':
        print('position:',4)
        category=Post.objects.get(slug=slug,id=id).category
        print('position:',5)
        if request.user.is_authenticated:
            print('body',Post.objects.get(slug=slug,id=id).body)
            context = {
            'post':Post.objects.get(slug=slug,id=id),
            'profile':Profile.objects.get(user=request.user),
            'tags':_all_post_tag(model=Post.objects.all()),
            'post_tags':_unique_list(arr=_hashtag(txt=Post.objects.filter(slug=slug)[0])),
            'categories':[c[0].title() for c in Post.CATEGORY],
            #not morethan 3
            
            'comment_form':CommentForm().as_p(),
            'popular_post':'',
            'related_post':Post.objects.filter(category=category).order_by('-pub_date')[:3],
            'latest_post':Post.objects.all().order_by('-pk')[:20],
            'locations':_unique_list([c.location.title() for c in Post.objects.all()]),
            
            }
        else:
            context = {
            'post':Post.objects.get(slug=slug,id=id),
            'tags':_all_post_tag(model=Post.objects.all()),
            'post_tags':_unique_list(arr=_hashtag(txt=Post.objects.filter(slug=slug)[0])),
            'categories':[c[0].title() for c in Post.CATEGORY],
            'popular_post':'',
            'related_post':Post.objects.filter(category=category).order_by('-pub_date')[:3],
            'latest_post':Post.objects.all().order_by('-pk')[:20],
            'locations':_unique_list([c.location.title() for c in Post.objects.all()]),
            
            }
        print('position:',6)
        return render(request, 'blog/blog-single.html', context)
        # return render(request, 'home.html', context)

    if request.method=='POST':
        print('position:',7)
        # print(request.POST)
        profile=Profile.objects.get(user=request.user)
        post=Post.objects.get(slug=slug,id=id)
        form=CommentForm(request.POST)
        # print('position:',8)
        # print('is this form valid',form.is_valid())
        # print('is this form bound',form.is_bound)
        # print('profile',profile)
        # print('post',post)
        # print('name',form.cleaned_data['name'])
        name =form.cleaned_data['name']
        email =form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        website = form.cleaned_data['website']
        # print('email',form.cleaned_data['email'])
        # print('comment',form.cleaned_data['comment'])
        # print('website',form.cleaned_data['website'])
        # print('pubdate',datetime.now())
        # print('is this form valid',form.is_valid())
        if form.is_valid:
            comment = Comment.objects.create(profile=profile,post=post,comment=comment,name=name,email=email,website=website,pub_date=datetime.now())

            return redirect(Post.objects.get(slug=slug,id=id))
        else:
            return redirect(Post.objects.get(slug=slug,id=id))
            redirect()


def about(request):
    context = {
        
    }
    return render(request, 'about.html', context)