class Venue:
    def __init__(self, **kwargs):
        name = kwargs['name']
        if isinstance(name, basestring):
            self.name = kwargs['name']
        else:
            raise TypeError('Did not pass string for venue name')
        
        self.review_list = []

class Review:
    def __init__(self, **kwargs):
        #venue must be a subclass of Venue
        venue = kwargs['venue']
        cost = kwargs['cost']
        num_guests = kwargs['num_guests']
        
        self.update_cost(cost)
        self.update_num_guests(num_guests)
        
        if isinstance(venue, Venue):
            self.venue = venue
        else:
            raise TypeError('Did not pass Venue subclass as venue parameter')
        
        #when review is created, add it to its venue's review list
        venue.review_list.append(self)
    
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


        