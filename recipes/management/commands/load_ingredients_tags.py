from django.core.management.base import BaseCommand
from recipes.models import Ingredient, Tag
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('recipes/data/ingredients.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                title, dimension = row
                Ingredient.objects.get_or_create(title=title, dimension=dimension)

        with open('recipes/data/tags.csv', encoding='utf-8') as file:
            file_reader = csv.reader(file)
            for tags in file_reader:
                Tag.objects.get_or_create(title=tags[0],
                                          display_name=tags[1],
                                          color=tags[2])
