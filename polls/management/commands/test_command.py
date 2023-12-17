from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('test_args', nargs='+', type=int)
        # parser.add_argument('arg2', nargs='*', default=[1,2,3])
        # parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
        parser.add_argument('numb', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        # QuestionAdmin.objects.bulk_create([Choice])
        fake = Faker()
        p = User.objects.bulk_create([User(
            username=fake.name(),
            email=fake.email(),
            password=make_password(fake.password())
        ) for _ in range(options['numb'])])


        # self.stdout.write(self.style.SUCCESS(f"Args: {options['test_args']}"))
        # self.stdout.write(self.style.SUCCESS(f"Arg2: {options['arg2']}"))
        self.stdout.write(self.style.SUCCESS(f"Arg2: {p}"))
