#Shell Table
'''
CREATE TABLE FeePolicy (
    policyID INT PRIMARY KEY,
    baseFee DECIMAL(10, 2) NOT NULL,
    maxFee DECIMAL(10, 2) NOT NULL
);
'''
import random

# Open a file to write the SQL statements
with open("fee_policy_data.sql", "w") as file:
    # Generate 25 policies
    for policy_id in range(1, 26):  # IDs from 1 to 25
        # Generate baseFee: only whole dollars between $5 and $10
        base_fee = random.randint(5, 10)
        
        # Determine maxFee based on baseFee range
        if base_fee in [5, 6, 7]:
            max_fee = 100
        else:  # base_fee in [8, 9, 10]
            max_fee = 300
        
        # Create the SQL statement
        sql_statement = (
            f"INSERT INTO FeePolicy (policyID, baseFee, maxFee) "
            f"VALUES ({policy_id}, {base_fee}.00, {max_fee}.00);\n"
        )
        
        # Write the statement to the file
        file.write(sql_statement)

print("SQL Insert statements saved to 'fee_policy_data.sql'.")
