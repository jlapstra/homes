from homes.models import Home
from django.core.management.base import BaseCommand
import csv
import datetime
import re

class Command(BaseCommand):
    help = 'Injest a csv file into Django models'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            reader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            first_row = next(reader)
            for row in reader:
                data = {}
                for i in range(22):
                    if row[i] == "":
                        data[first_row[i]] = None
                    elif re.match(r"\d{2}\/\d{2}\/\d{4}", row[i]):
                        data[first_row[i]] = datetime.datetime.strptime(row[i], "%m/%d/%Y").strftime("%Y-%m-%d")
                    else:
                        data[first_row[i]] = row[i]

                home = Home(**data)
                home.save()
                self.stdout.write(
                    'Created {} Home: {}'.format(home.home_type, home.zillow_id)
                )


