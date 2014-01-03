class Venue:
    def __init__(self, **kwargs):
        '''
        Construct a Venue object
        
        Required parameters: name (a string)
        Will throw KeyError without the name parameters
        '''
        name = kwargs['name']
        self.update_name(name)
        
        self.review_list = []
        
        #Add venue to the list of venues
        if 'venue_list' in kwargs:
            kwargs['venue_list'].add(self)
    
    def update_name(self, name):
        if isinstance(name, basestring):
            self.name = name
        else:
            raise TypeError('Did not pass string for venue name')
    
    def add_review(self, review):
        if review not in self.review_list:
            self.review_list.append(review)
            return True
        else:
            return False
    
    def calculate_average_cost(self):
        '''
        Calculate the average cost from all the venue's reviews
        
        Returns None if there are no reviews
        '''
        if len(self.review_list) == 0:
            return None
        else:
            #calculate sum using generator that gets the costs of each review
            return float(sum((review.cost for review in self.review_list)))/len(self.review_list)

class Review:
    def __init__(self, **kwargs):
        '''
        Construct a Review object
        
        Required parameters:
        venue (a string)
        cost (a number)
        num_guests (prefereably an int - will be cast as an int)
        
        Will throw a KeyError without these parameters
        '''
        #venue must be a subclass of Venue
        venue = kwargs['venue']
        cost = kwargs['cost']
        num_guests = kwargs['num_guests']
        
        self.update_cost(cost)
        self.update_num_guests(num_guests)
        self.update_venue(venue)
    
    def update_venue(self, venue):
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
            
        
    
    def update_cost(self, cost):
        '''
        Update the cost attribute
        Throw ValueError if cost is less than or equal to 0
        '''
        if cost > 0:
            self.cost = cost
        else:
            raise ValueError('cost must be greater than 0')
    
    def update_num_guests(self, num_guests):
        '''
        Update the number of guests
        Throw ValueError if number of guests is less than or equal to 0
        '''
        num_guests = int(num_guests)
        if num_guests > 0:
            self.num_guests = num_guests
        else:
            raise ValueError('num_guests must be greater than 0')

class VenueList:
    def __init__(self):
        '''
        Construct a VenueList object
        No parameters necessary
        '''
        self._venue_list = []
    
    def add(self,venue):
        '''Add venue to list of venues'''
        self._venue_list.append(venue)
    
    def get_venue(self, venue_name):
        '''
        Get the venue with the same name as the venue_name parameter
        If there is none, throw Key Error
        '''
        venue_name = venue_name.lower()
        for venue in self._venue_list:
            if venue.name.lower() == venue_name:
                return venue
        
        return None


        