import csv

from django.core.management.base import BaseCommand

from map.models import Squirrel

def str_to_bool(s):
    if s.lower() == 'true':
         return True
    elif s.lower() == 'false':
         return False
    else:
         raise ValueError # evil ValueError that doesn't tell you what the wrong value was

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for item in data:
            p = Squirrel(
                    Latitude=item['X'],
                    Longitude=item['Y'], 
                    UniqueSquirrelID=item['Unique Squirrel ID'],
                    Shift=item['Shift'],
                    Date=item['Date'],
                    Age=item['Age'],
                    PrimaryFurColor=item['Primary Fur Color'],
                    Location=item['Location'],
                    SpecificLocation=item['Specific Location'],
                    Running=str_to_bool(item['Running']),
                    Chasing=str_to_bool(item['Chasing']),
                    Climbing=str_to_bool(item['Climbing']),
                    Eating=str_to_bool(item['Eating']),
                    Foraging=str_to_bool(item['Foraging']),
                    OtherActivities=item['Other Activities'],
                    Kuks=str_to_bool(item['Kuks']),
                    Quaas=str_to_bool(item['Quaas']),
                    Moans=str_to_bool(item['Moans']),
                    Tailflags=str_to_bool(item['Tail flags']),
                    Tailtwitches=str_to_bool(item['Tail twitches']),
                    Approaches=str_to_bool(item['Approaches']),
                    Indifferent=str_to_bool(item['Indifferent']),
                    Runsfrom=str_to_bool(item['Runs from']),
            )
            p.save()
