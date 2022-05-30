from realpath import realpath


class WriteDataFromLocalFile:
    def __init__(self) -> None:
        self.__fwrite = open(
            f"{realpath}/resources/subscription.txt", "w", encoding="UTF8"
        )

    def write(self, data):
        """write uploaded data in file"""

        with self.__fwrite as f:

            f.writelines(str(data))
