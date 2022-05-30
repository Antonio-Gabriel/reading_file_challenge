from unittest import TestCase

from mapper.MappingDataFromFile import MappingDataFromFile


class TestMappingDataFromFile(TestCase):
    def test_mapping_data_from_file(self):

        """Extract data from file"""

        mapping_file = MappingDataFromFile()

        """Trying for return a file data"""
        file_data = (
            mapping_file
            .extract_content_to_file_and_add_to_array()
            )

        # [FILE] > assert list data
        self.assertTrue(file_data, "The file doesn't have data")
