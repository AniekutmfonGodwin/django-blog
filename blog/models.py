from django.db import models
from django.utils.text import slugify
# from ckeditor.fields import  RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField
from django.conf import settings
from django.urls import reverse
from .utility import _hashtag,_unique_list

# Create your models here.




class Profile(models.Model):
    profile_pic = models.ImageField(verbose_name='Profile Photo',upload_to='profile',help_text='Profile Photo')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    facebook = models.URLField( max_length=200,null=True,blank=True)
    instagram = models.URLField( max_length=200,null=True,blank=True)
    twitter = models.URLField( max_length=200,null=True,blank=True)
    youtube = models.URLField( max_length=200,null=True,blank=True)
    about_me = models.TextField(max_length=500,help_text='A short description about yourself')

    def __str__(self):
        return self.user.username
 

class Post(models.Model):
    CATEGORY=[
    ('Lifestyle','Lifestyle'),
    ('Travel','Travel'),
    ('Food','Food'),
    ('Adventure','Adventure'),
    ('Business','Business'),
]
    slug = models.SlugField(default='', blank=True)
    title = models.CharField(verbose_name="Post Title",max_length=300,help_text='Enter your title')
    category = models.CharField(max_length=250,choices=CATEGORY, help_text='Select category')
    featured_image = models.ImageField(verbose_name='Upload Featured Image', upload_to='bolg',help_text='Upload featured Image',default='media_root/default_featured.jpg')
    body = RichTextUploadingField(blank=True,null=True)
    tags = models.CharField(verbose_name='Tag',max_length=500,help_text='Seperate tags with comma "," ',null=True,blank=True)
    location = models.CharField(verbose_name='Location',max_length=200,help_text='enter location', blank=True,null=True)
    pub_date = models.DateTimeField(verbose_name='Date Publish',auto_now=True)
    # detail = RichTextField(blank=True,null=True)
    published = models.BooleanField(verbose_name='Publish post',default=False,help_text='publish post')



    @property
    def comment(self):
        return self.comment_set.all()
    
    @property
    def get_tags(self):
        return _unique_list(arr=_hashtag(self.tags))

    @property
    def comment_count(self):
        return len(self.comment_set.all())


    def save(self):
        self.slug = slugify(self.title)
        super(Post, self).save()

    def get_absolute_url(self):
        return reverse("blog:single",kwargs={'slug':self.slug,'id':self.id})

    def __str__(self):
        return '%s' % self.title



class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    comment = models.TextField(verbose_name='Comment', max_length=300)
    name = models.CharField(verbose_name='Name',max_length=250)
    email = models.EmailField(verbose_name='Email', max_length=100)
    website = models.URLField( max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)


    


    def __str__(self):
        return '%s' % self.comment

