from django.core.management.base import BaseCommand
from actresses.models import Actress

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        actress_names = [
            "Scarlett Johansson",
            "Emma Watson",
            "Margot Robbie",
            "Jennifer Lawrence",
            "Ana de Armas",
            "Zendaya",
            "Sydney Sweeney",
            "Alexandra Daddario",

            "Elizabeth Olsen",
            "Gal Gadot",
            "Megan Fox",
            "Angelina Jolie",
            "Natalie Portman",
            "Anne Hathaway",
            "Emma Stone",
            "Jessica Alba",

            "Monica Bellucci",
            "Penelope Cruz",
            "Charlize Theron",
            "Salma Hayek",
            "Kate Beckinsale",
            "Eva Mendes",
            "Mila Kunis",
            "Dakota Johnson",

            "Jennifer Aniston",
            "Jessica Biel",
            "Blake Lively",
            "Amber Heard",
            "Margaret Qualley",
            "Sydney Meyer",

            "Aishwarya Rai",
            "Priyanka Chopra",
            "Deepika Padukone",
            "Katrina Kaif",
            "Alia Bhatt",
            "Shraddha Kapoor",
            "Kriti Sanon",
            "Tamannaah Bhatia",
            "Rashmika Mandanna",
            "Kiara Advani",
            "Disha Patani",
            "Ananya Panday",
            "Janhvi Kapoor",
            "Sara Ali Khan",
            "Mrunal Thakur",
            "Pooja Hegde",
            "Nora Fatehi",

            "Adriana Lima",
            "Bella Hadid",
            "Gigi Hadid",
            "Irina Shayk",
            "Emily Ratajkowski",
            "Kate Upton",

            "Selena Gomez",
            "Ariana Grande",
            "Taylor Swift",
            "Rihanna",
            "Dua Lipa",
            "Beyonce",
            "Shakira",
            "Katy Perry",
            "Camila Cabello",
            "Madison Beer",

            "Galina Dubenenko",
            "Barbara Palvin",
            "Lily Collins",
            "Sophie Turner",
            "Phoebe Tonkin",
            "Lily James"
        ]

        for name in actress_names:

            actress, created = Actress.objects.get_or_create(name=name)

            if created:
                print(f"Added {name}")
            else:
                print(f"{name} already exists")