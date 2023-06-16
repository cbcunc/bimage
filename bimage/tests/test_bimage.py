"""Tests for the bimage module."""


import unittest
from bimage import bimage
import os
import shutil


class TestBimage(unittest.TestCase):
    """Test functions in the bimage module."""

    def setUp(self):
        """Test fixture build."""
        
        bimage.bimage("cbcunc", "timage", "develop")

    def tearDown(self):
        """Test fixture destroy."""
        
        shutil.rmtree("timage")

    def test_bimage(self):
        """Test bimage.bimage."""

        self.assertTrue(os.path.exists("timage"))

