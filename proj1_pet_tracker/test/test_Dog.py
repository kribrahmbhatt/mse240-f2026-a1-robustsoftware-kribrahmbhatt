import unittest
from ..dog.Dog import Dog

class TestDog(unittest.TestCase):
    """ TestDog

        Unit test for the Dog class
    """


    def setUp(self):
        """ set up typical examples for each test """
        self._typicaldog1_waffle = Dog("Waffle", "Newfoundland", 
                                        "Male", 130, "Black", 
                                        ["geriatric hips"], 2018)
        self._typicaldog2_george = Dog("George", "Goldendoodle",
                                        "Male", 145, "Brown",
                                        [], 2020)
    

    #
    # Constructor Tests
    #


    def test_constructor_typical1(self):
        dog = self._typicaldog1_waffle
        self.assertEqual("Waffle", dog.get_name())
        self.assertEqual("Newfoundland", dog.get_breed())
        self.assertEqual("Male", dog.get_gender())
        self.assertAlmostEqual(130, dog.get_weight())
        self.assertEqual("Black", dog.get_colour())
        self.assertEqual(["geriatric hips"], dog.get_potential_health_issues())
        self.assertEqual(6, dog.get_age())

    def test_constructor_typical2(self):
        dog = self._typicaldog2_george
        self.assertEqual("George", dog.get_name())
        self.assertEqual("Goldendoodle", dog.get_breed())
        self.assertEqual("Male".lower(), dog.get_gender().lower())
        self.assertAlmostEqual(145, dog.get_weight())
        self.assertEqual("Brown", dog.get_colour())
        self.assertEqual([], dog.get_potential_health_issues())
        self.assertEqual(4, dog.get_age())
        
    def test_constructor_valueerror_emptyname(self):
        with self.assertRaises(ValueError):
            dog = Dog("", "Newfoundland", 
                  "Male", 130, "Black", 
                  ["geriatric hips"], 2018)

    def test_constructor_typeerror_numericname(self):
        """ Test for TypeError in the dog's name """
        with self.assertRaises(TypeError):
            dog = Dog(3, "Newfoundland", 
                  "Male", 130, "Black", 
                  ["geriatric hips"], 2018)
        with self.assertRaises(TypeError):
            dog = Dog(3.2, "Newfoundland", 
                  "Male", 130, "Black", 
                  ["geriatric hips"], 2018)
        with self.assertRaises(TypeError):
            dog = Dog(-8, "Newfoundland", 
                  "Male", 130, "Black", 
                  ["geriatric hips"], 2018)

    def test_constructor_valueerror_negativeweight(self):
        with self.assertRaises(ValueError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", -130, "Black", 
                  ["geriatric hips"], 2018)
        with self.assertRaises(ValueError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", -0.01, "Black", 
                  ["geriatric hips"], 2018)

    def test_constructor_valueerror_maxweight(self):
        with self.assertRaises(ValueError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", 750, "Black", 
                  ["geriatric hips"], 2018)
        with self.assertRaises(ValueError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", 500.1, "Black", 
                  ["geriatric hips"], 2018)
        

    def test_constructor_typeerror_weight(self):
        with self.assertRaises(TypeError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", "500", "Black", 
                  ["geriatric hips"], 2018)
        with self.assertRaises(TypeError):
            dog = Dog("Waffle", "Newfoundland", 
                  "Male", [1, 2, 3], "Black", 
                  ["geriatric hips"], 2018)

    #...







    #############
    # Accessors #
    #############

    
    #
    # get_name
    #
    
    def test_get_name_typical1(self):
        self.assertEqual("Waffle", self._typicaldog1_waffle.get_name())

    def test_get_name_typical2(self):
         self.assertEqual("George", self._typicaldog2_george.get_name())

    #
    # get_breed
    #

    def test_get_breed_typical1(self):
        self.assertEqual("Newfoundland", self._typicaldog1_waffle.get_breed())

    def test_get_breed_typical2(self):
        self.assertEqual("Goldendoodle", self._typicaldog2_george.get_breed())