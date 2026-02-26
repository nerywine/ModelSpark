# test_modelspark.py
"""
Tests for ModelSpark module.
"""

import unittest
from modelspark import ModelSpark

class TestModelSpark(unittest.TestCase):
    """Test cases for ModelSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelSpark()
        self.assertIsInstance(instance, ModelSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
