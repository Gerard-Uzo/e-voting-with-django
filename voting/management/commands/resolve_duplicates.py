from django.core.management.base import BaseCommand
from voting.models import Voter
from collections import Counter

class Command(BaseCommand):
    help = 'Resolve duplicate matric_number values in the Voter table.'

    def handle(self, *args, **kwargs):
        voters = Voter.objects.all()
        matric_numbers = [voter.matric_number for voter in voters]
        duplicates = [item for item, count in Counter(matric_numbers).items() if count > 1]

        for duplicate in duplicates:
            duplicate_voters = Voter.objects.filter(matric_number=duplicate)
            for index, voter in enumerate(duplicate_voters):
                if index > 0:  # Keep the first occurrence, modify the rest
                    voter.matric_number = f"{voter.matric_number}_{index}"
                    voter.save()

        self.stdout.write(self.style.SUCCESS('Duplicate matric_number values resolved.'))