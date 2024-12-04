Here’s a formatted version of your setup guide, optimized for GitHub with Markdown syntax:

```markdown
# Setup Guide for Library Management System Database

This guide will help you set up the **Library Management System Database** on your local machine using **MySQL**.

## Prerequisites

- **MySQL**: Ensure MySQL is installed on your system. You can download it from [MySQL Downloads](https://dev.mysql.com/downloads/).
- **MySQL Client**: Use MySQL Workbench, or the MySQL command-line client to run the SQL scripts.

---

## Step 1: Create the Database

1. **Connect to MySQL**: Open your MySQL client and connect to your local MySQL server.

   ```bash
   mysql -u root -p
   ```

2. **Create the Database**: Run the following command to create the database.
   ```sql
   CREATE DATABASE library_management;
   ```

3. **Select the Database**: Switch to the newly created database.
   ```sql
   USE library_management;
   ```

---

## Step 2: Run SQL Scripts

You will find the necessary SQL scripts in the `DDL/` and `Data/` folders. These scripts need to be executed in sequence.

### 2.1: Create Tables

Run the `create_tables.sql` script to create the necessary tables in the database.

```sql
SOURCE /path/to/DDL/create_tables.sql;
```

### 2.2: Insert Sample Data

Run the following scripts in order to populate the tables with sample data:

1. `author_data.sql`
2. `publisher_data.sql`
3. `user_data.sql`
4. `fee_policy_data.sql`
5. `resource_data.sql`
6. `borrowing_data.sql`

```sql
SOURCE /path/to/Data/author_data.sql;
SOURCE /path/to/Data/publisher_data.sql;
SOURCE /path/to/Data/user_data.sql;
SOURCE /path/to/Data/fee_policy_data.sql;
SOURCE /path/to/Data/resource_data.sql;
SOURCE /path/to/Data/borrowing_data.sql;
```

### 2.3: Add Constraints

Run the `constraints.sql` script to define constraints like primary and foreign keys.

```sql
SOURCE /path/to/DDL/constraints.sql;
```

---

## Step 3: Verify the Setup

Once the scripts have been executed, perform the following checks to verify the setup:

### 3.1: Check Tables

Ensure that the tables were created successfully.

```sql
SHOW TABLES;
```

### 3.2: Check Data

Verify that the sample data has been inserted correctly.

```sql
SELECT * FROM members;
```

### 3.3: Check Triggers

Test that the triggers work, for example, by simulating an overdue borrowing and checking if late fees are calculated.

### 3.4: Check Views

Test the views by running a query, e.g., to check the most borrowed books:

```sql
SELECT * FROM most_borrowed_books;
```

---

## Step 4: Running Queries

The `Queries/` folder contains SQL queries for generating reports and performing data analysis. To run any query, execute the SQL file in your MySQL client.

For example, to view the borrowing history, run:

```sql
SOURCE /path/to/Queries/Search_and_Reports/user_borrowing_history.sql;
```

---

## Conclusion

After completing these steps, the Library Management System database should be fully set up and ready to use. If you encounter any issues, refer to the `testing_report.md` for troubleshooting, or consult the `final_report.md` for more detailed project information.
```

This layout uses proper Markdown syntax for better readability and formatting on GitHub. Simply copy and paste this into your repository's README.md or any other Markdown file.
