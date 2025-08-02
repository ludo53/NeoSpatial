# test_neospatial.py
"""
Tests for NeoSpatial module.
"""

import unittest
from neospatial import NeoSpatial

class TestNeoSpatial(unittest.TestCase):
    """Test cases for NeoSpatial class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoSpatial()
        self.assertIsInstance(instance, NeoSpatial)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoSpatial()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
