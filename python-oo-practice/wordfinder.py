"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    ...
class WordFinder:

    def __init__(self, path):

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} word read")

    def parse(self, dict_file):

        return [w.strip() for w in dict_file]

    def random(self):

        return random.choice(self.words) 

    class SpecialWOrdFinder(WordFinder):

        def parse(self, dict_file):

            return [w.strip() for w in dict_file
                    if w.strip() and not w.startwith('#')]
