from django.db import models

from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):
    unique_squirrel_id = models.CharField(
        help_text=_('Unique Squirrel ID Number'),
        max_length=50,
    )

    longitude = models.DecimalField(
        help_text='Longitude coordinate for squirrel sighting point',
        max_digits=15,  # learn from data
        decimal_places=10,
    )

    latitude = models.DecimalField(
        help_text='Latitude coordinate for squirrel sighting point',
        max_digits=15,  # learn from data
        decimal_places=10,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM, 'AM'),
                     (PM, 'PM'))

    shift = models.CharField(
        help_text=_('Shift in the day'),
        max_length=2,
        choices=SHIFT_CHOICES,
    )

    date = models.DateField(
        help_text='Concatenation of the sighting session day and month.',
    )

    ADULT = 'Adult'
    JUVENILEE = 'Juvenilee'
    
    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILEE, 'Juvenilee'),
    )

    age = models.CharField(
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

    primary_fur_color = models.CharField(
        help_text=_('Primary Fur Color of squirrel'),
        max_length=16,
        choices=FUR_CHOICES,
    )

    ABOVE = 'Above Ground'
    GROUND = 'Ground Plane'
    
    LOCATION_CHOICES = (
        (ABOVE, 'Above Ground'),
        (GROUND, 'Ground Plane'),
    )

    location =  models.CharField(
        help_text=_('Location of squirrel'),
        max_length=16,
        choices=LOCATION_CHOICES,
    )

    specific_location = models.CharField(
        help_text=_('Specific Location'),
        max_length=255,
        blank=True,
    )

    running = models.BooleanField(
        help_text='If squirrel is running',
        default=False,
    )

    chasing = models.BooleanField(
        help_text='If squirrel is chasing',
        default=False,
    )

    climbing = models.BooleanField(
        help_text='If squirrel is climbing',
        default=False,
    )

    eating = models.BooleanField(
        help_text='If squirrel is eating.',
        default=False,
    )

    foraging = models.BooleanField(
        help_text='If squirrel is foraging.',
        default=False,
    ) 

    other_activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=255,
        blank=True,
    )

    kuks = models.BooleanField(
        help_text='Squirrel was heard kukking.',
        default=False,
    )

    quaas = models.BooleanField(
        help_text='Squirrel was heard quaaing.',
        default=False,
    )

    moans = models.BooleanField(
        help_text='Squirrel was heard moaning',
        default=False,
    )

    tail_flags = models.BooleanField(
        help_text='Squirrel was seen flagging its tail.',
        default=False,
    )

    tail_twitches = models.BooleanField(
        help_text='Squirrel was seen twitching its tail. ',
        default=False,
    )

    approaches = models.BooleanField(
        help_text='Squirrel was seen approaching human, seeking food.',
        default=False,
    )

    indifferent = models.BooleanField(
        help_text='Squirrel was indifferent to human presence.',

    )

    runs_from = models.BooleanField(
        help_text='Squirrel was running from humans, seeing them as a threat.',
        default=False,
    )   

    def __str__(self):
        return self.unique_squirrel_id