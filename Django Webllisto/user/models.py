from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        # in case these fields are not entered during creation
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)


        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')


        return self.create_user(email, user_name, first_name, password, **other_fields)

    def create_user(self, email, user_name, first_name, password, **other_fields):
        # since email is required
        if not email:
            raise ValueError(_('You must provide an email address'))
        

        # format the email, like lowercase the domain part etc
        email = self.normalize_email(email)


        user = self.model(email=email, user_name=user_name,
                          first_name=first_name, **other_fields)
        user.set_password(password)
        user.save()
        return user



# AbstractBaseUser: for extending the django user functionalities
# PermissionMixin: for handling the user permissions in django


class NewUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_(
        'about'), max_length=500, blank=True)
    

    # since these fields are required by django backend
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    # our custom manager for this class
    objects = CustomAccountManager()


    # the field which is used for logging in
    USERNAME_FIELD = 'email'

    # the fields that are required for creating superuser
    REQUIRED_FIELDS = ['user_name', 'first_name']


    def __str__(self):
        return self.user_name


# ******************************** CUSTOM QUERYSET

# now we'll use manager, custom queryset to 
# get all the post in descending order of created_at




class PostQuerySet(models.QuerySet):
    # this method takes a queryset object and alters it how
    # we want.
    # so now we can use Post.objects.all().sorted()
    #  to get the queryset that we want
    def sorted(self):
        return self.order_by('-created_at')


class PostManager(models.Manager):

    # now we can use Post.objects.sorted() to get the 
    # queryset we want
    def sorted(self):
        # get_queryset() returns all the instances of the
        #  current class

        # return self.get_queryset().order_by("-created_at")

        
        # but now we don't need this, since the QuerySet 
        # class has a sorted() method in itself
        
        # so we can redefine the class Queryset, so that it
        # has another method sorted, which will give us the 
        # data we want
        return self.get_queryset().sorted()

    # returns queryset object containing all the objects
    def get_queryset(self):

        # returning the custom queryset class object 
        # instead of the predefined queryset class
        return PostQuerySet(model=self.model, using=self._db)


class PostManager2(models.QuerySet):

    # now we can use Post.objects.sorted() to get the 
    # queryset we want
    def sorted(self):
        # get_queryset() returns all the instances of the
        #  current class

        # return self.get_queryset().order_by("-created_at")

        
        # but now we don't need this, since the QuerySet 
        # class has a sorted() method in itself
        
        # so we can redefine the class Queryset, so that it
        # has another method sorted, which will give us the 
        # data we want
        return self.order_by("-created_at")



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # set the manager as custom manager
    # objects = PostManager()
    objects = PostManager2().as_manager()

    def __str__(self):
        return self.title
 




# Post.objects.sorted()
# Post.sorted()



class Product(models.Model):

    
    suppliers = (
        ("Supplier1", "sup1"),
        ("Supplier2", "sup2"),
        ("Supplier3", "sup3"),
        ("Supplier4", "sup4"),
        ("Supplier5", "sup5"),
    )

    supplier = models.CharField(choices = suppliers,max_length= 100, null = True, blank = True)
    
    name = models.CharField(max_length=50)
    
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name




