## Schema Documentation

### Relational Schema Diagram
The relational schema diagram is a visual representation showing all relations, attributes, primary keys, and foreign keys. (The diagram can be created using a tool like Lucidchart or draw.io.)

### Data Dictionary

The data dictionary documents each relation, its attributes, data types, domains, and constraints, providing a clear reference for developers.

| Relation   | Attribute       | Data Type   | Description                               |
|------------|-----------------|-------------|-------------------------------------------|
| **User**   | userID          | INT         | Unique identifier for each user           |
|            | name            | VARCHAR     | User's name                               |
|            | role            | ENUM        | Role of the user in the system            |
|            | email           | VARCHAR     | User's email address                      |
|            | phone           | VARCHAR     | User's phone number                       |
| **Resource** | resourceID    | INT         | Unique identifier for each resource       |
|            | title           | VARCHAR     | Title of the resource                     |
|            | type            | ENUM        | Type of resource (e.g., Book, Magazine)   |
|            | authorID        | INT         | Reference to the resource's author        |
|            | publisherID     | INT         | Reference to the resource's publisher     |
|            | availableCopies | INT         | Number of copies available for borrowing  |
|            | totalCopies     | INT         | Total copies of the resource              |
| **Borrowing** | borrowID     | INT         | Unique identifier for each borrowing event|
|            | userID          | INT         | Reference to the borrowing user           |
|            | resourceID      | INT         | Reference to the borrowed resource        |
|            | borrowDate      | DATE        | Date of borrowing                         |
|            | returnDate      | DATE        | Date of return                            |
|            | dueDate         | DATE        | Due date for returning the resource       |
|            | lateFee         | DECIMAL     | Fee for late returns                      |
| **Author** | authorID        | INT         | Unique identifier for each author         |
|            | name            | VARCHAR     | Author's name                             |
|            | biography       | TEXT        | Information about the author              |
| **Publisher** | publisherID  | INT         | Unique identifier for each publisher      |
|            | name            | VARCHAR     | Publisher's name                          |
|            | address         | VARCHAR     | Publisher's address                       |

