import unittest
from ..sampleclass.sampleclass import SampleClass


class SampleClassBaseTestCase(unittest.TestCase):
    """
    Base class for SampleClass test cases.
    Implements setUp() for every test case that inherits it.
    """

    def setUp(self):
        """ sets up typical and unusual cases"""

        # TODO: comment
        self._sc_typical1 = SampleClass("name", 1)

        #TODO: comment
        self._sc_typical2 = SampleClass("Oliver's bicycle", 499.99)