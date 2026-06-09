# Elementary School Treasurer Management System

An automated system for managing student accounts, bills, payments, and balance tracking to eliminate manual auditing.

## Features

✅ **User Authentication** - Secure login with encrypted passwords (bcrypt)
✅ **Student Management** - Add, edit, view, and delete student records
✅ **Billing & Payments** - Track bills and payments with real-time balance calculation
✅ **Transaction History** - Complete audit trail with timestamps
✅ **Reports** - Student balance summaries and collection status
✅ **Dashboard** - Overview of financial status
✅ **Responsive UI** - Web-based interface with Bootstrap

## System Requirements

- Python 3.9+
- MySQL 5.7+ or MariaDB
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Rayyjcray/elementary-treasury-system.git
cd elementary-treasury-system
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database

Create the database and tables:

```bash
mysql -u your_username -p < setup_db.sql
```

Or manually execute the SQL commands in `setup_db.sql` in your MySQL client.

### 5. Configure Database Connection

Edit `config.py` and update your MySQL credentials:

```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/elementary_treasury'
```

### 6. Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Default Credentials

After setup, you can create a new account by clicking "Register" or use the admin setup script.

## Usage

### Login
- Navigate to the login page
- Enter your username and password
- Click "Login"

### Dashboard
- View overview of financial status
- See recent transactions
- Access quick links to main features

### Student Management
- **View Students**: Click "Students" to see all students
- **Add Student**: Click "Add Student" button
- **Edit Student**: Click edit icon next to student name
- **Delete Student**: Click delete icon to remove student

### Add Bills & Payments
- Click "Add Transaction"
- Select student
- Choose transaction type (Bill or Payment)
- Enter amount and description
- Add transaction

### View Student Details
- Click on any student name
- View complete transaction history
- See current balance
- View all bills and payments

### Reports
- Click "Reports"
- View student balance summary
- Download collection status
- Check outstanding payments

## Database Schema

### users
- user_id (Primary Key)
- username (Unique)
- password_hash (Encrypted)
- email
- created_at

### students
- student_id (Primary Key)
- student_name
- grade_section

### ledger
- transaction_id (Primary Key)
- student_id (Foreign Key)
- transaction_type (BILL or PAYMENT)
- description
- amount
- date_stamp
- time_stamp

## Security Features

✅ Encrypted password storage using bcrypt
✅ Session-based authentication
✅ CSRF protection
✅ SQL injection prevention with parameterized queries
✅ Input validation and sanitization

## File Structure

```
elementary-treasury-system/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── database.py            # Database models & functions
├── setup_db.sql           # Database initialization script
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── students.html
│   ├── add_student.html
│   ├── student_detail.html
│   ├── add_transaction.html
│   ├── reports.html
│   └── all_transactions.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Troubleshooting

### MySQL Connection Error
- Verify MySQL is running
- Check username and password in `config.py`
- Ensure database name is correct

### Module Not Found Error
- Make sure virtual environment is activated
- Run `pip install -r requirements.txt` again

### Port Already in Use
- Change the port in `app.py` (default 5000)
- Or close the application using port 5000

## Features in Detail

### Real-time Balance Calculation
The system automatically calculates:
- **Student Balance** = Total Bills - Total Payments
- Updates in real-time as transactions are added
- Shows outstanding amount for each student

### Transaction Timestamps
Every transaction records:
- Date stamp (YYYY-MM-DD)
- Time stamp (HH:MM:SS)
- User who made the transaction
- Complete audit trail

### Reports
- **Student Balance Report**: All students with current balances
- **Collection Status**: Payment collection overview
- **Outstanding Payments**: Students with unpaid bills
- **Transaction History**: Detailed transaction logs

## Support

For issues or suggestions, please create an issue on GitHub.

## License

This project is open source and available under the MIT License.

---

**Version**: 1.0.0
**Last Updated**: 2026-06-09
