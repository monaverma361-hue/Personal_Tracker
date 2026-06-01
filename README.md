# Personal Expense Manager

A beginner-friendly expense tracking web app built with Streamlit and SQLite. This project helps users record daily expenses, review recent transactions, filter expenses by date range, generate summary totals, export CSV files, and delete records when needed.

## Features

- Add expense entries through a simple Streamlit form
- Store expense data in a local SQLite database
- View the latest 10 transactions
- Filter expense history by date range
- Show category-wise total expense summary for a selected date range
- Export all expenses to CSV
- Export filtered expenses by date range to CSV
- Delete expenses by date range with confirmation
- Delete all expenses with confirmation

## Screenshots

Add screenshots after pushing the project to GitHub.

- `assets/home-page.png`
- `assets/expense-history.png`
- `assets/manage-data.png`

Example Markdown you can use later:

```md
![Home Page](assets/home-page.png)
![Expense History](assets/expense-history.png)
![Manage Data](assets/manage-data.png)
```

## Project Structure

```text
Personal_Tracker/
├── app/
│   └── main.py
├── core/
│   ├── expenses.py
│   └── managedata.py
├── data/
│   └── document.db
├── db/
│   ├── database.py
│   └── repositry.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used

- Python 3.13
- Streamlit
- Pandas
- SQLite

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Personal_Tracker
```

### 2. Create a virtual environment

On macOS/Linux:

```bash
python3 -m venv .venv
```

On Windows:

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

From the project root, run:

```bash
streamlit run app/main.py
```

After running the command, Streamlit will open a local URL in your browser, usually:

```text
http://localhost:8501
```

## Example Workflow

1. Open the app in your browser.
2. Go to the `Add Expense` tab.
3. Enter values for grocery, dairy, laundry, shopping, fruit and vegetable, other bills, payment mode, and date.
4. Click `Enter` to save the expense.
5. Go to the `View Expenses` tab to see recent transactions.
6. Select a date range to filter expense history.
7. Click `Show Total Summary` to view category-wise totals.
8. Go to the `Manage Data` tab to export or delete records.

## Database Notes

- The project uses SQLite, so no separate database server is required.
- The database file is created locally inside the `data/` folder.
- Expense records are stored in the `expenses` table.

## Future Improvements

- Add charts and expense analytics dashboard
- Add category validation and better form input controls
- Add monthly and yearly reports
- Add edit/update functionality for saved expenses
- Add user authentication for multi-user support
- Add cloud deployment configuration

## Author

**Mona Verma**

If you are using this project as a portfolio project, you can also add:

- GitHub profile link
- LinkedIn profile link
- Portfolio website link

## Python Version

This project was developed with **Python 3.13.7**.

It is a good idea to mention the Python version in this `README.md`. You do not need to put the Python version inside `requirements.txt`.
