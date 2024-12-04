
# Setup Guide for Library Management System Database

This guide will help you set up the **Library Management System Database** on your local machine using **MySQL**.

## Prerequisites

- **MySQL**: Ensure MySQL is installed on your system. You can download it from [MySQL Downloads](https://dev.mysql.com/downloads/).
- **MySQL Client**: Use MySQL Workbench, or the MySQL command-line client to run the SQL scripts.

## Step 1: Create the Database

1. **Connect to MySQL**: Open your MySQL client and connect to your local MySQL server.

   ```bash
   mysql -u root -p

Create the Database: Run the following command to create the database.
CREATE DATABASE library_management;
Select the Database: Switch to the newly created database.
USE library_management;
Step 2: Run SQL Scripts

You will find the necessary SQL scripts in the DDL/ and the Data/ folder. These scripts need to be executed in sequence.

2.1: Create Tables
Run the create_tables.sql script to create the necessary tables in the database.

SOURCE /path/to/DDL/creat_tables.sql;

2.2: Insert Sample Data
Run author_data.sql, publisher_data.sql, user_data.sql, fee_policy_data.sql, resource_data.sql, and borrowing_data.sql scripts in that order to populate the tables with sample data.

SOURCE /path/to/Data/Data_files;


Step 3: Verify the Setup

Once the scripts have been executed, verify the setup by performing the following checks:

Check Tables
Ensure that the tables were created successfully.

SHOW TABLES;
Check Data
Verify that the sample data has been inserted correctly.

SELECT * FROM members;
Check Triggers
Test that the triggers work, for example, by simulating an overdue borrowing and checking if late fees are calculated.

Check Views
Test the views by running a query, e.g., to check the most borrowed books:

SELECT * FROM most_borrowed_books;
Step 4: Running Queries

The Queries/ folder contains SQL queries for generating reports and performing data analysis. To run any query, simply execute the SQL file in your MySQL client.

For example, to view the borrowing history, run:

SOURCE /path/to/Queries/Search_and_Reports/user_borrowing_history.sql;
Conclusion

After completing these steps, the Library Management System database should be fully set up and ready to use. If you encounter any issues, refer to the testing_report.md for troubleshooting, or consult the final_report.md for more detailed project information.


