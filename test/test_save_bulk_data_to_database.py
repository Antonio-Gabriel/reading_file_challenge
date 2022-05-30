from unittest import TestCase

from mapper.MappingDataFromFile import MappingDataFromFile
from system.SaveBulkDataFileToDatabase import SaveBulkDataFileToDatabase


class TestSaveBulkData(TestCase):
    def test_save_bulk_data_to_database(self):

        # specify table name for bulk insert into table
        create_attr = SaveBulkDataFileToDatabase(
            "venda", MappingDataFromFile()
            )

        save_result = create_attr.save_bulk_data_attr()

        print("\n")

        # [RESULT] > affected_rows: , total_records_from_file:
        
        self.assertTrue(save_result, "Bulk register")
