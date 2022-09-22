#Adam Grinde
#21/09
#Utomhusklasser


class mcdonalds():
    """A class representing a Mcdonalds"""

    def __init__(self, location, decor, size, rating):
        """For the McDonalds location and rating of the McDonalds"""
        self.location = location.title()
        self.decor = decor
        self.size = size
        self.rating = rating


    def describe_mcdonalds(self):
        """Display a review of the McDonalds"""
        msg = "McDonalds " + self.location + ", decor is " + self.decor + ", it's " + self.size + " and the total rating out of 10 is " + self.rating + "."
        print("\n" + msg)

    def open_mcdonalds(self):
        """Display a message that the McDonalds is open"""
        msg = "McDonalds " + self.location + " is open. Welcome in!"
        print("\n" + msg)


    """List of the reviewed resturants"""
mcdonaldsnacka = mcdonalds('Nacka', 'good', 'large', '7')
mcdonaldstyreso = mcdonalds('Tyresö', 'bad', 'pretty small', '4')
mcdonaldscity = mcdonalds('City', 'Average', 'medium sized', '6')

print( "McDonalds " + mcdonaldsnacka.location)

print(mcdonaldsnacka.rating)

mcdonaldsnacka.describe_mcdonalds()
mcdonaldsnacka.open_mcdonalds()

input("To get a review of the next resturant please press enter:")

print( "McDonalds " + mcdonaldstyreso.location)

print(mcdonaldstyreso.rating)

mcdonaldstyreso.describe_mcdonalds()
mcdonaldstyreso.open_mcdonalds()

input("To get a review of the next resturant please press enter:")

print( "McDonalds " + mcdonaldscity.location)

print(mcdonaldscity.rating)

mcdonaldscity.describe_mcdonalds()
mcdonaldscity.open_mcdonalds()


