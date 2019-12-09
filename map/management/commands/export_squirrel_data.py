from django.core.management.base import BaseCommand, CommandError
import csv
import sys
from map.models import Squirrel
from django.apps import apps


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *app_labels, **options):
        with open(options['csv_file'], 'w') as fp:
            model = apps.get_model('map', 'Squirrel')
            field_names = [f.name for f in model._meta.fields]
            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)

            writer.writerow(field_names)
            for instance in model.objects.all():
                writer.writerow([getattr(instance, f) for f in field_names])
