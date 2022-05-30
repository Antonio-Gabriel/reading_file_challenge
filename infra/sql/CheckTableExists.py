from .connector import cursor


def checkTableExists(table_name: str):
    """check if table exists on database"""

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(
            table_name.replace("'", "''")
        )
    )
    if cursor.fetchone()[0] == 1:        
        return True
    
    return False
