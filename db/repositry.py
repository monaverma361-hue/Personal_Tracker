from db.database import get_connection


class InsertExpenses():

    def insert_expense(
            self,
            grocery,
            dairy,
            laundry,
            payment_mode,
            shopping,
            fruit_vegetable,
            other_bills,
            date,
        ):
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO expenses(
                    grocery,
                    dairy,
                    laundry,
                    payment_mode,
                    shopping,
                    fruit_vegetable,
                    other_bills,
                    date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    grocery,                     
                    dairy,
                    laundry,
                    payment_mode,
                    shopping,
                    fruit_vegetable,
                    other_bills,
                    date,
                ),
            )

            conn.commit()
            conn.close()


    

