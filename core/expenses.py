from db.database import get_connection


class ExpenseManager:


    

    def get_last10_expenses(self):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM expenses

            ORDER BY id DESC

            LIMIT 10

        """)

        data = cursor.fetchall()

        conn.close()
        

        return data

    def get_expenses_by_date_range(self, start_date, end_date):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT * FROM expenses

            WHERE date BETWEEN ? AND ?

            ORDER BY date ASC

        """, (start_date, end_date))

        data = cursor.fetchall()

        conn.close()

        return data
    
    def get_total_expenses_by_date_range(self, start_date, end_date):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT 

                SUM(grocery),

                SUM(dairy),

                SUM(laundry),

                SUM(shopping),

                SUM(fruit_vegetable),

                SUM(other_bills)

            FROM expenses

            WHERE date BETWEEN ? AND ?

        """, (start_date, end_date))

        data = cursor.fetchone()

        conn.close()

        return data