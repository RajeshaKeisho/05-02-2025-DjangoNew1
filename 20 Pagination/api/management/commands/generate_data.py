from django.core.management.base import BaseCommand
from utils.fake_data import generate_all_data

class Command(BaseCommand):
    help = 'Generates fake data for testing purposes'

    def handle(self, *args, **options):
        generate_all_data()
        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))