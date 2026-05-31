import pandas as pd
import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from core.expenses import ExpenseRepository

data = [

    [1, 1200, 350, 150, "UPI", 800, 600, 450, "2026-03-01"],

    [2, 950, 200, 100, "Cash", 1200, 500, 300, "2026-03-03"],

    [3, 1500, 400, 180, "Credit Card", 600, 750, 500, "2026-03-05"],

    [4, 800, 250, 120, "UPI", 900, 450, 250, "2026-03-08"],

    [5, 1100, 300, 200, "Debit Card", 700, 550, 400, "2026-03-10"],

]

df = pd.DataFrame(

    data,

    columns=[

        "id",

        "grocery",

        "dairy",

        "laundry",

        "payment_mode",

        "shopping",

        "fruit_vegetable",

        "other_bills",

        "date"

    ]

)

startdate = "2026-03-03"

enddate = "2026-03-08"

obj = ExpenseRepository()

print(obj.get_total_expenses_by_date_range(startdate,enddate))