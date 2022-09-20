from pyexpat import model
from django.db import models
from stdimage.models import StdImageField

from django.db.models import signals
from django.template.defaultfilters import slugify

class Posts(models.Model):
    typePost = models.CharField('Category', max_length=50)
    titlePost = models.CharField('Title', max_length=120)
    descriptionPost = models.CharField('Description', max_length=220)
    image = StdImageField(upload_to='articles', variations={'thumbnail': {"width": 292, "height": 330, "crop": True}})
    slug = models.SlugField('slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return  str(self.titlePost)


class PostDetail(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    contentPost = models.TextField('Content')

class Profile(models.Model):
    nameProfile = models.CharField('Nome', max_length=100)
    gitLink = models.CharField('Git', max_length=100)
    linkedinLink = models.CharField('Linkedin', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)
    hello = models.CharField('Hello', max_length=50)
    congratulation = models.CharField('Congratulation', max_length=200)
    apresentation = models.CharField('Apresentation', max_length=200)
    history = models.TextField('History')
    emailProfile = models.EmailField('Email')
    locate = models.CharField('Locate', max_length=150)
    phone = models.CharField('Phone', max_length=20)
    image = StdImageField(upload_to='articles', variations={'thumbnail': {"width": 292, "height": 330, "crop": True}})


    def __str__(self):
        return  str('Profile')    

def slug_pre_save_posts(signal, instance, sender, **kg):
    instance.slug = slugify(instance.titlePost)

signals.pre_save.connect(slug_pre_save_posts, sender=Posts)


