#Shell Table
'''
CREATE TABLE Resource (
    resourceID INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    type ENUM('Book', 'Magazine', 'Digital Media') NOT NULL,
    authorID INT,
    publisherID INT,
    availableCopies INT NOT NULL,
    totalCopies INT NOT NULL,
    FOREIGN KEY (authorID) REFERENCES Author(authorID),
    FOREIGN KEY (publisherID) REFERENCES Publisher(publisherID)
);
'''
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Open a file to write the SQL statements
with open("resource_data.sql", "w") as file:
    # Generate 10,000 resources
    for resource_id in range(1, 10001):  # IDs from 1 to 10000
        # Generate random data
        title = fake.sentence(nb_words=4)  # Generate a random title with 4 words
        resource_type = random.choice(['Book', 'Magazine', 'Digital Media'])  # Random type
        author_id = random.randint(1, 2000)  # AuthorID between 1 and 2000
        publisher_id = random.randint(1, 1000)  # PublisherID between 1 and 1000
        total_copies = random.randint(1, 200)  # Total copies between 1 and 200
        available_copies = random.randint(0, total_copies)  # Available copies <= Total copies
        
        # Create the SQL statement
        sql_statement = (
            f"INSERT INTO Resource (resourceID, title, type, authorID, publisherID, availableCopies, totalCopies) "
            f"VALUES ({resource_id}, '{title}', '{resource_type}', {author_id}, {publisher_id}, {available_copies}, {total_copies});\n"
        )
        
        # Write the statement to the file
        file.write(sql_statement)

print("SQL Insert statements saved to 'resource_data.sql'.")