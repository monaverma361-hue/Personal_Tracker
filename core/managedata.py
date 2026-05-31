from db.database import get_connection

class DataManagment():

    def get_all_expenses_for_export(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM expenses

            ORDER BY id ASC

        """)

        data = cursor.fetchall()

        conn.close()

        return data
