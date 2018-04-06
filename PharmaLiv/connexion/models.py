from django.db import models
from django.contrib.auth import models as usermodels


# Create your models here.
class User(usermodels.AbstractUser):
    """
    AbstractUser
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    User
    User within the Django authentication system are represented by this
    model.
    """ 
    is_patient= models.BooleanField(default=False)
    is_medecin= models.BooleanField(default=False)
    is_livreur = models.BooleanField(default=False)
    is_pharmacie=models.BooleanField(default = False)
    is_userbi = models.BooleanField(default=False )
    

