from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class Image_TestCases(TestCase):
    def setUp(self):


        self.new_neighb  = Neighbourhood(id ='1',name ='Runda',location = 'Westland',occupants = '10',user_id ='1')
        self.new_comment = Comment(id='1',user_id = '1',photo = 'articles/default.jpg',comment = 'Welcome',post_date = '23-03-2019')
        self.new_business = Business(id='1',photo = 'articles/NoPic.png',name ='Java',user_id = '1',neighbourhood_id = '1',email = 'me@you.com')
        self.new_profile = Profile(id ='1', NeighName_id ='1',user_id = '1',profile_pic='media/articles/Nature.jpg',bio='The one and only admin', contact='07190000')
        self.new_neighb.save_neighb()
        self.new_comment.save_comment()
        self.new_business.save_business()
        self.new_profile.save_profile()


    def tearDown(self):
        Neighbourhood.objects.all().delete()
        Comment.objects.all().delete()
        Business.objects.all().delete()
        Profile.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_neighb,Neighbourhood))
        self.assertTrue(isinstance(self.new_comment,Comment))
        self.assertTrue(isinstance(self.new_business,Business))
        self.assertTrue(isinstance(self.new_profile,Profile))

    def test_save_method(self):
        self.new_neighb.save_neighb()
        new_neighb = Neighbourhood.objects.all()
        self.assertTrue(len(new_neighb)>0)

    def test_delete_method(self):
        self.new_neighb.save_neighb()
        new_neighb = Neighbourhood.objects.filter(name='Runda')
        Neighbourhood.delete_neigborhood(new_neighb)
        neigh = Neighbourhood.objects.all()
        self.assertTrue(len(neigh) == 0)
