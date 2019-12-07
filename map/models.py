from django.db import models

from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    Latitude = models.FloatField(
        help_text=_('Latitude of Squirrel'),
        max_length=50,
    )

    Longitude = models.FloatField(
        help_text=_('Longitude of Squirrel'),
        max_length=50,
    )
    UniqueSquirrelID = models.CharField(
        help_text=_('Unique Squirrel ID Number'),
        max_length=50,
    )

    Shift = models.CharField(
        help_text=_('Shift in the day'),
        max_length=2,
    )

    Date = models.CharField(
        help_text=_('Squirrel Come Date'),
        max_length=2,
    )

    ADULT = 'Adult'
    JUVENILEE = 'Juvenilee'
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILEE, 'Juvenilee'),
    )

    Age = models.CharField(
        help_text=_('Age of squirrel'),
        max_length=16,
        choices=AGE_CHOICES,
    )

    CINNAMONT = 'Cinnamont'
    BLACK = 'Black'
    GRAY = 'Gray'
    
    FUR_CHOICES = (
        (CINNAMONT, 'Cinnamont'),
        (BLACK, 'Black'),
        (GRAY, 'Gray'),
    )

    PrimaryFurColor = models.CharField(
        help_text=_('Primary Fur Color of squirrel'),
        max_length=16,
        choices=FUR_CHOICES,
    )

    ABOVE = 'Above Ground'
    GROUND = 'Ground Plane'
    
    LOCATIONCHOICES = (
        (ABOVE, 'Above Ground'),
        (GROUND, 'Ground Plane'),
    )

    Location =  models.CharField(
        help_text=_('Location of squirrel'),
        max_length=16,
        choices=LOCATIONCHOICES,
    )

    SpecificLocation = models.CharField(
        help_text=_('Specific Location'),
        max_length=100,
    )

    Running = models.BooleanField(
        help_text='If squirrel is running'
    )

    Chasing = models.BooleanField(
        help_text='If squirrel is chasing'
    )

    Climbing = models.BooleanField(
        help_text='If squirrel is climbing'
    )

    Eating = models.BooleanField(
        help_text='If squirrel is eating'
    )

    Foraging = models.BooleanField(
        help_text='If squirrel is foraging'
    ) 

    OtherActivities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
    )

    Kuks = models.BooleanField(
        help_text='Kuks'
    )

    Quaas = models.BooleanField(
        help_text='Quaas'
    )

    Moans = models.BooleanField(
        help_text='Moans'
    )

    Tailflags = models.BooleanField(
        help_text='Tail flag'
    )

    Tailtwitches = models.BooleanField(
        help_text='Tail twitches'
    )

    Approaches = models.BooleanField(
        help_text='Approachesg'
    )

    Indifferent = models.BooleanField(
        help_text='Indifferent'
    )

    Runsfrom = models.BooleanField(
        help_text='Runs fromg'
    )   

    def __str__(self):
        return self.name