import csv

from django.core.management.base import BaseCommand

from map.models import Pet


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
