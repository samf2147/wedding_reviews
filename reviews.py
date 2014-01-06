__all__ = ['Venue', 'Review']

class Venue:
    def __init__(self, name, **kwargs):
        '''
        Construct a Venue object
        
        Required parameters: name (a string)
        '''
        
        self.set_name(name)
        self.reviews = set()

    
    def set_name(self, name):
        if isinstance(name, basestring):
            self.name = name
        else:
            raise TypeError('Did not pass string for venue name')
    
    def add_review(self, review):
        self.reviews.add(review)
    
    def calculate_average_cost(self):
        '''
        Calculate the average cost from all the venue's reviews
        
        Returns None if there are no reviews
        '''
        if len(self.reviews) == 0:
            return None
        else:
            #calculate sum using generator that gets the costs of each review
            return float(sum((review.cost for review in self.reviews)))/len(self.reviews)


class Review:
    def __init__(self, venue, cost, num_guests):
        '''
        Construct a Review object
        
        Required parameters:
        venue (a string)
        cost (a number)
        num_guests (prefereably an int - will be cast as an int)
        
        Will throw a KeyError without these parameters
        '''
        #venue must be a subclass of Venue        
        self.set_cost(cost)
        self.set_num_guests(num_guests)
        self.set_venue(venue)
    
    def set_venue(self, venue):
        '''
        Update the venue of the review object
        Throws TypeError if it's not passed a Venue object
        '''
        #check to make sure you're updating to a Venue object
        if not isinstance(venue, Venue):
            raise TypeError('Did not pass Venue subclass as venue parameter')
        else:
            self.venue = venue
            venue.add_review(self)
              
    def set_cost(self, cost):
        '''
        Update the cost attribute
        Throw ValueError if cost is less than or equal to 0
        '''
        if cost > 0:
            self.cost = cost
        else:
            raise ValueError('cost must be greater than 0')
    
    def set_num_guests(self, num_guests):
        '''
        Update the number of guests
        Throw ValueError if number of guests is less than or equal to 0
        '''
        num_guests = int(num_guests)
        if num_guests > 0:
            self.num_guests = num_guests
        else:
            raise ValueError('num_guests must be greater than 0')


        