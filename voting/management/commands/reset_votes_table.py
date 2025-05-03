from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Remove invalid foreign key references in the voting_votes table.'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA foreign_keys = OFF;")  # Disable foreign key checks
            cursor.execute("DELETE FROM voting_votes;")  # Remove all rows in voting_votes
            cursor.execute("PRAGMA foreign_keys = ON;")  # Re-enable foreign key checks
        self.stdout.write(self.style.SUCCESS('Invalid foreign key references removed from voting_votes table.'))