#Shell Table
'''
CREATE TABLE Borrowing (
    borrowID INT PRIMARY KEY,
    userID INT NOT NULL,
    resourceID INT NOT NULL,
    borrowDate DATE NOT NULL,
    returnDate DATE,
    dueDate DATE NOT NULL,
    lateFee DECIMAL(10, 2),
    policyID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (resourceID) REFERENCES Resource(resourceID),
    FOREIGN KEY (policyID) REFERENCES FeePolicy(policyID)
);
'''
import random
from datetime import datetime, timedelta

# Open a file to write the SQL statements
with open("borrowing_data.sql", "w") as file:
    # Generate 6,000 borrowing records
    for borrow_id in range(1, 6001):  # IDs from 1 to 6,000
        # Random userID and resourceID
        user_id = random.randint(1, 5000)
        resource_id = random.randint(1, 10000)
        
        # Random borrow date within the past year
        borrow_date = datetime.now() - timedelta(days=random.randint(1, 365))
        borrow_date_str = borrow_date.strftime('%Y-%m-%d')
        
        # Due date: 7 to 30 days after borrow date
        due_date = borrow_date + timedelta(days=random.randint(7, 30))
        due_date_str = due_date.strftime('%Y-%m-%d')
        
        # Return date: Randomly determine if the resource has been returned
        if random.random() < 0.8:  # 80% chance the resource has been returned
            return_date = borrow_date + timedelta(days=random.randint(1, (due_date - borrow_date).days + 15))
            return_date_str = return_date.strftime('%Y-%m-%d')
        else:
            return_date_str = "NULL"
        
        # Late fee: Calculate if returnDate > dueDate
        if return_date_str != "NULL" and datetime.strptime(return_date_str, '%Y-%m-%d') > due_date:
            days_late = (datetime.strptime(return_date_str, '%Y-%m-%d') - due_date).days
            late_fee = round(days_late * random.uniform(0.50, 5.00), 2)  # Late fee per day: $0.50–$5.00
        else:
            late_fee = "NULL"
        
        # Random policyID
        policy_id = random.randint(1, 25)
        
        # Create the SQL statement
        sql_statement = (
            f"INSERT INTO Borrowing (borrowID, userID, resourceID, borrowDate, returnDate, dueDate, lateFee, policyID) "
            f"VALUES ({borrow_id}, {user_id}, {resource_id}, '{borrow_date_str}', {return_date_str}, '{due_date_str}', {late_fee}, {policy_id});\n"
        )
        
        # Write the statement to the file
        file.write(sql_statement)

print("SQL Insert statements saved to 'borrowing_data.sql'.")