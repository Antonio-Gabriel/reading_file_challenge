import mysql.connector
from mysql.connector import errorcode

from infra.sql.connector import conn, cursor


class GenericRepository:
    def __init__(self, table_name: str) -> None:
        self.__table_name = table_name

    def save_bulk(self, headers: list, contents: list):

        try:
            headers_attrs = " ".join(headers).replace(" ", ", ")
            dynamic_values = " ".join(("%s " * len(headers)).split()).replace(" ", ", ")

            mySql_insert_query = f"""
                INSERT INTO {self.__table_name} (
                    {headers_attrs}
                    ) 
                VALUES ({dynamic_values}) """

            array_to_tuple = map(tuple, contents)
            tuple_of_tuples = tuple(array_to_tuple)

            records_to_insert = [*tuple_of_tuples]

            cursor.executemany(mySql_insert_query, records_to_insert)
            conn.commit()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_TABLE_ERROR:
                print("Creating table spam")
            else:
                raise
        
        #cursor.close()

        return cursor.rowcount
