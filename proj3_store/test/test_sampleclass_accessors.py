# test_sampleclass_accessors
#
# Author: Oliver Schneider
# Email: 
# Student ID: 1234567890
#
# these are the unit tests for SampleClass


import unittest
from ..test import SampleClassBaseTestCase
from ..sampleclass.sampleclass import SampleClass


class TestSampleClassAccessors(SampleClassBaseTestCase):

    #TODO: comment
    def test_getname_typical1(self):
        sc = self._sc_typical1
        self.assertEqual(sc.get_name(), "name")


    #TODO: comment
    def test_getprice_typical1(self):
        sc = self._sc_typical1
        self.assertAlmostEqual(sc.get_price(), 1)


    #TODO: complete the test cases for the accessors