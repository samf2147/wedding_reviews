import unittest
from reviews import Venue, Review

class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.venue_one = Venue(name='Surf Club')
        self.venue_two = Venue(name=u'Greentree')
        self.review_one = Review(venue = self.venue_one, cost = 10000.00, num_guests = 200)
        self.review_two = Review(venue = self.venue_one, cost = 20000.00, num_guests = 500)
        self.review_three = Review(venue = self.venue_two, cost = 20000.00, num_guests=30.5)
        
    
    def test_venue_constructors(self):
        self.assertEqual(self.venue_one.name, 'Surf Club')
        self.assertEqual(self.venue_two.name, 'Greentree')
    
    def test_review_constructors(self):
        #test the venue for actual object identity
        self.assertTrue(self.review_one.venue is self.venue_one) 
        self.assertEqual(self.review_one.cost, 10000.00)
        self.assertEqual(self.review_one.num_guests, 200)
        
    
    def test_out_of_bounds_assignments(self):
        #can't enter string for venue name
        self.assertRaises(TypeError, Venue, name=5)
        
        #venue must be a venue object
        self.assertRaises(TypeError, Review, venue = 'Surf Club', cost = 10000.00, num_guests = 200)
        
        #cost and num_guests must both be greater than 0
        self.assertRaises(ValueError, Review, venue = self.venue_one, cost = 0, num_guests = 200)
        self.assertRaises(ValueError, Review, venue = self.venue_one, cost = 10000.00, num_guests = 0)
        
        #after construction, num_guests must be an int
        self.assertTrue(isinstance(self.review_three.num_guests,int))
    
    def test_review_in_venue_list(self):
        #check that creating the revue adds it to the venue's list
        self.assertTrue(self.review_one in self.venue_one.reviews)
        self.assertTrue(self.review_three not in self.venue_one.reviews)
        self.assertEqual(len(self.venue_one.reviews),2)
        
        #prevent duplicate reviews
        self.venue_one.add_review(self.review_one)
        self.assertEqual(len(self.venue_one.reviews),2)
        
    
    def test_set_review(self):
        self.review_two.set_cost(15000.00)
        self.assertEqual(self.review_two.cost, 15000.00)
        
        self.review_two.set_num_guests(160)
        self.assertEqual(self.review_two.num_guests,160)
        
        #review_three is the only review for venue 2
        set_venue_result = self.review_three.set_venue(self.venue_one)
        self.assertTrue(self.review_three.venue is self.venue_one)
    
    
    def test_venue_average_cost(self):
        self.assertAlmostEqual(self.venue_one.calculate_average_cost(), 15000.00)
        self.dummy_venue = Venue(name='Fake venue')
        self.assertEqual(self.dummy_venue.calculate_average_cost(), None)


        
        