#Shell Table
'''
CREATE TABLE Author (
    authorID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);
'''
from faker import Faker

# Initialize Faker
fake = Faker()

# Open a file to write the SQL statements
with open("author_data.sql", "w") as file:
    # Generate 2000 authors
    for author_id in range(1, 2001):  # IDs from 1 to 2000
        # Generate realistic author data
        name = fake.name()  # Random name
        biography = fake.paragraph(nb_sentences=5)  # Short biography with 5 sentences

        # Escape single quotes for SQL
        name = name.replace("'", "''")
        biography = biography.replace("'", "''")

        # Create the SQL statement
        sql_statement = (
            f"INSERT INTO Author (authorID, name, biography) "
            f"VALUES ({author_id}, '{name}', '{biography}');\n"
        )
        
        # Write the statement to the file
        file.write(sql_statement)

print("Author SQL Insert statements saved to 'author_data.sql'.")
