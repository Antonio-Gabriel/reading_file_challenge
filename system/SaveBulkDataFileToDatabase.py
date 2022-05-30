from typing import Type

from tabulate import tabulate
from utils.text_conversor import text_conversor

from mapper.MappingDataFromFile import MappingDataFromFile
from infra.repository.GenericRepository import GenericRepository

class SaveBulkDataFileToDatabase:
    def __init__(self, table_name: str, mapper: Type[MappingDataFromFile]) -> None:
        self.__mapper = mapper
        self.__generic_repo = GenericRepository(table_name)

    def save_bulk_data_attr(self) -> list:
        """get headers from list and create dynamic attributes to database"""
        
        attrs = (
            self.__mapper
            .extract_content_to_file_and_add_to_array()
            )        

        headers = []
        for attr in attrs[0]:
            # strip text and convert to lower
            attr_converted = text_conversor(attr)
            headers.append(attr_converted)
        
        # delete headers
        del attrs[0]

        # debug table preview
        custom_tabulate = tabulate(attrs, headers=headers)
        print(custom_tabulate)     
                
        # # save bulk
        affected_rows = self.__generic_repo.save_bulk(
            headers,
            attrs
        )

        if affected_rows == 0:

            unlink_result = self.__mapper.unlink_content_to_file()

            return {
                "error": {
                    "status": 404,
                    "msg": "Table not exists",
                    "unlink": unlink_result
                }
            }
      
        unlink_result = self.__mapper.unlink_content_to_file()

        return {
            "success": {
                "status": 200,
                "affected_rows": affected_rows,
                "total_records_from_file": len(attrs),
                "unlink": unlink_result,
                "data": attrs
            }
        }