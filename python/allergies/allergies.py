map = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}


class Allergies(object):
    def __init__(self, score):
        self.score = score
        self.lst = [allergy for allergy in map if self.is_allergic_to(allergy)]

    def is_allergic_to(self, allergen):
        return map[allergen] & self.score
