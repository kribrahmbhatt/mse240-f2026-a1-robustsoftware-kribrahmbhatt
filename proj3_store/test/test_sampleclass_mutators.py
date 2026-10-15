# test_sampleclass_mutators
#
# Author: Oliver Schneider
# Email: 
# Student ID: 1234567890
#
# these are the unit tests for SampleClass


import unittest
from ..test import SampleClassBaseTestCase
from ..sampleclass.sampleclass import SampleClass


class TestSampleClassMutators(SampleClassBaseTestCase):

   
    #TODO: comment
    def test_setname_typical1(self):
        sc = self._sc_typical1
        self.assertEqual(sc.get_name(), "name")
        sc.set_name("new name")
        self.assertEqual(sc.get_name(), "new name")


    #TODO: comment
    def test_setprice_typical1(self):
        sc = self._sc_typical1
        self.assertAlmostEqual(sc.get_price(), 1)
        sc.set_price(9.99)
        self.assertAlmostEqual(sc.get_price(), 9.99)


    #TODO: complete the test cases for the mutators