class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year_of_creation):
        self.title = title
        self.painter = painter
        self.year_of_creation = year_of_creation


painting_1 = Painting(input(), input(), input())
print('"' + painting_1.title + '"' + " by " + painting_1.painter + " (" + painting_1.year_of_creation + ") hangs in the " + painting_1.museum + ".")
