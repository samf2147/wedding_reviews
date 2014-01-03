class Venue:
    def __init__(self, **kwargs):
        name = kwargs['name']
        if isinstance(name, basestring):
            self.name = kwargs['name']
        else:
            raise TypeError(message = 'Did not pass string for venue name')

class Review:
    def __init__(self, **kwargs):
        self.venue = kwargs['venue']
        self.cost = kwargs['cost']
        self.num_guests = kwargs['num_guests']
        