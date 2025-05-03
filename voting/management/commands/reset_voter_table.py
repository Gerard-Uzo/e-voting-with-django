from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Drop and recreate the voting_voter table to resolve schema issues.'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys = OFF;")  # Disable foreign key checks
            cursor.execute("DROP TABLE IF EXISTS voting_voter;")
            cursor.execute("PRAGMA foreign_keys = ON;")  # Re-enable foreign key checks
        self.stdout.write(self.style.SUCCESS('voting_voter table dropped successfully.'))