from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Creating ExO Roles ...')

        call_command('loaddata', '1_roles_exo_sprint')
        call_command('loaddata', '2_roles_fastrack')
        call_command('loaddata', '3_roles_workshop')
        call_command('loaddata', '4_roles_swarm')
        call_command('loaddata', '5_roles_summit')

        self.stdout.write(self.style.SUCCESS('ExO Roles created!'))
