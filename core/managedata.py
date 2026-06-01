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
    
    def delete_expenses_by_date_range(self, start_date, end_date):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM expenses

            WHERE date BETWEEN ? AND ?

        """, (start_date, end_date))

        conn.commit()

        conn.close()

    def delete_all_expenses(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM expenses

        """)

        conn.commit()

        conn.close()
