from realpath import realpath


class MappingDataFromFile:
    def __init__(self, mode: str = "r") -> None:
        self.__fopen = open(
            f"{realpath}/resources/subscription.txt", mode, encoding="UTF8", newline=""
        )

    def extract_content_to_file_and_add_to_array(self) -> list:
        """extract contents from subcription file"""

        data_array = []
        with self.__fopen as f:
            """Read file data"""

            data = f.read().splitlines()
            for row in data:

                if not row:
                    f.close()
                    break

                data_array.append(row.split("\t"))

        return data_array

    def unlink_content_to_file(self):
        """remove extracted content to local file"""
        self.__init__("w")

        with self.__fopen as f:
            """subscribe local file to empty"""

            f.write("")

            return "Remove extracted content to local file"
