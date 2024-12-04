#Shell Table
'''
CREATE TABLE User (
    userID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Member') NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    status ENUM('Active', 'Expired', 'Suspended') NOT NULL,
    membershipValidUntil DATE
);
'''
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Open a file to write the SQL statements
with open("users_data.sql", "w") as file:
    # Generate 5000 users
    for user_id in range(1, 5001):  # IDs from 1 to 5000
        # Generate random data
        name = fake.name()  # Random name
        # Ensure ~5% are Admins
        role = 'Admin' if user_id <= 250 else 'Member'
        email = fake.unique.email()  # Unique email
        
        # Generate a phone number limited to 20 characters
        phone = fake.phone_number()
        if len(phone) > 20:
            phone = phone[:20]
        
        # Random status
        status = random.choice(['Active', 'Expired', 'Suspended'])
        
        # Generate a membership valid date: today or in the future if active
        if status == 'Active':
            membership_valid_until = (datetime.now() + timedelta(days=random.randint(30, 365))).date()
        else:  # Set a past date for non-active statuses
            membership_valid_until = (datetime.now() - timedelta(days=random.randint(1, 365))).date()
        
        # Create the SQL statement
        sql_statement = (
            f"INSERT INTO User (userID, name, role, email, phone, status, membershipValidUntil) "
            f"VALUES ({user_id}, '{name}', '{role}', '{email}', '{phone}', '{status}', '{membership_valid_until}');\n"
        )
        
        # Write the statement to the file
        file.write(sql_statement)

print("SQL Insert statements saved to 'users_data.sql'.")