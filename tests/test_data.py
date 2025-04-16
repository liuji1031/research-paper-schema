"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from research_paper_schema.datamodel.research_paper_schema import ResearchPaperCollection

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            obj = yaml_loader.load(path, target_class=ResearchPaperCollection)
            assert obj
