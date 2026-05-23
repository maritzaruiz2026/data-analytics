class restaurant:
    """A class is created to represent a resturant and food types available"""
    def __init__ (self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []


    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}.')

    def rest_open(self):
        print(f'{self.rest_name} is open.')

    def add_number_served(self, number_served):
        self.number_served += number_served

    def print_number_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers.')

    def customer_rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            average = sum(self.customer_ratings)/ len(self.customer_ratings)
            print(f'Your rating was {rating}.') #removed at first since it kept outputting "Your rating was" for every rating added, but it would not output the error message if I removed it
            print(f'The average rating for this restaurant is {average}') ## I couldn't figure out how to display JUST the last average rating
            #I also could not figure out how to display JUST ine rating as "Your raating was..." and hide the other ratings
        else:
            print("Invalid entry. Your rating must be between 1-5 to be included in store rating average.")

restaurant_1 = restaurant("Weedy's", "American")
restaurant_2 = restaurant("Zacatacos", "Mexican")
restaurant_3 = restaurant("Olivio Garden", "Italian")
                          
restaurant_1.describe_rest()
restaurant_1.rest_open()
restaurant_1.add_number_served(2)
restaurant_1.print_number_served()
restaurant_1.customer_rating(9) ## number was invalid so it wasn't accounted for at first
restaurant_1.customer_rating(3)

restaurant_2.describe_rest()
restaurant_2.rest_open()
restaurant_2.add_number_served(5)
restaurant_2.print_number_served()
restaurant_2.customer_rating(2)
restaurant_2.customer_rating(5)
restaurant_2.customer_rating(7) ## number was invalid so it wasn't accounted for at first
restaurant_2.customer_rating(1)
restaurant_2.customer_rating(4)

restaurant_3.describe_rest()
restaurant_3.rest_open()
restaurant_3.add_number_served(3)
restaurant_3.print_number_served()
restaurant_3.customer_rating(4)
restaurant_3.customer_rating(1)
restaurant_3.customer_rating("5 stars") # number was invalid so it wasn't accounted for st first