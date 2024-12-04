#Shell Table
'''
CREATE TABLE Publisher (
    publisherID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255)
);
'''
from faker import Faker

# Initialize the Faker instance
fake = Faker()

# Open a file to write the SQL statements
with open("publishers_data.sql", "w") as file:
    # Generate 1000 publishers
    for publisher_id in range(1, 1001):  # IDs from 1 to 1000
        # Generate random data
        name = fake.company()  # Random company name
        address = fake.address().replace("\n", " ")  # Random address (replace newlines with space)
        
        # Create the SQL statement
        sql_statement = f"INSERT INTO Publisher (publisherID, name, address) VALUES ({publisher_id}, '{name}', '{address}');\n"
        
        # Write the statement to the file
        file.write(sql_statement)

print("SQL Insert statements saved to 'publishers_data.sql'.")
