# test_sampleclass_constructor
#
# Author: Oliver Schneider
# Email: 
# Student ID: 1234567890
#
# these are the unit tests for SampleClass


import unittest
from ..test import SampleClassBaseTestCase
from ..sampleclass.sampleclass import SampleClass


class TestSampleClassConstructor(SampleClassBaseTestCase):

    #TODO: comment
    def test_constructor_typical1(self):
        sc = self._sc_typical1
        self.assertIsNotNone(sc)
        self.fail()


    #TODO: comment
    def test_constructor_typical2(self):
        sc = self._sc_typical2
        self.assertIsNotNone(sc)
        self.fail()


    #TODO: complete the test cases for the constructor