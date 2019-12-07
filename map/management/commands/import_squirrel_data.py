import csv

from django.core.management.base import BaseCommand

from map.models import Squirrel


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
                    Running=item['Running'],
                    Chasing=item['Chasing'],
                    Climbing=item['Climbing'],
                    Eating=item['Eating'],
                    Foraging=item['Foraging'],
                    OtherActivities=item['Other Activities'],
                    Kuks=item['Kuks'],
                    Quaas=item['Quaas'],
                    Moans=item['Moans'],
                    Tailflags=item['Tail flags'],
                    Tailtwitches=item['Tail twitches'],
                    Approaches=item['Approaches'],
                    Indifferent=item['Indifferent'],
                    Runsfrom=item['Runs from'],
            )
            p.save()
