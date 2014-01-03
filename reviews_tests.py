import unittest
from reviews import Venue, Review

class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.venue_one = Venue(name='Surf Club')
        self.venue_two = Venue(name=u'Greentree')
        self.review_one = Review(venue = self.venue_one, cost = 10000.00, num_guests = 200)
        self.review_two = Review(venue = self.venue_one, cost = 20000.00, num_guests = 500)
    
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
        