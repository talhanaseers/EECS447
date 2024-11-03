# Library Management System: Logical Relational Schema Documentation

## 1. Introduction

### Project Overview
The Library Management System database is designed to efficiently manage a library's inventory, including books, digital media, and magazines, while tracking client memberships, borrowing activities, and imposing late fees for overdue items. The system facilitates resource management, borrowing rules, and late fee calculations, while supporting multi-user interactions through transaction management and role-based access control. This system aims to enhance library operations and user experience.

### Scope
The project will focus on developing a relational database supporting core library functionalities, including resource management, user management, and borrowing operations with late fees. It enforces borrowing limits and borrowing durations, tracks overdue items, and supports multi-user transactions with role-based access for different user roles (Admins, Members). Excluded functionalities include non-library-related services, financial transactions outside of library fees, and any resources unrelated to the library’s collection.

### Glossary
- **Library Resource:** Any item available for borrowing, such as books, digital media, and magazines.
- **Borrowing Rules:** Constraints on the number of items a user can borrow and the borrowing duration.
- **Late Fees:** Fines imposed on users for overdue borrowed items.
- **User Role:** Specific access level assigned to a user (e.g., Admin, Member).
- **Foreign Key:** A field in a relational table that uniquely identifies a row in another table, ensuring data integrity between relations.
- **Transaction Management:** Ensures reliable application of all database changes in multi-user scenarios.
- **Admin Users:** Users responsible for managing library resources, user accounts, and generating reports.
- **Member Users:** End-users who borrow and return resources, manage accounts, and pay overdue fees.
- **Normalization:** The process of organizing data to reduce redundancy and improve integrity, potentially applied in future schema refinements.

---

## 2. Relational Schema Mapping

### Identify Relations
For each entity and relationship set in the ER diagram, a corresponding relation (table) is created:
- **User** 
- **Resource**
- **Borrowing**
- **Author**
- **Publisher**

### Define Attributes and Domains
Each attribute in the entity and relationship sets is defined with a corresponding attribute in the appropriate relation, along with data types and domain constraints.

| Relation   | Attribute       | Data Type   | Domain/Constraint              |
|------------|-----------------|-------------|--------------------------------|
| **User**   | userID          | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | role            | ENUM        | ('Admin', 'Member')            |
|            | email           | VARCHAR     | Unique, Not Null               |
|            | phone           | VARCHAR     |                                |
| **Resource** | resourceID    | INT         | Primary Key                    |
|            | title           | VARCHAR     | Not Null                       |
|            | type            | ENUM        | ('Book', 'Magazine', 'Digital Media') |
|            | authorID        | INT         | Foreign Key (Author)           |
|            | publisherID     | INT         | Foreign Key (Publisher)        |
|            | availableCopies | INT         | Not Null                       |
|            | totalCopies     | INT         | Not Null                       |
| **Borrowing** | borrowID     | INT         | Primary Key                    |
|            | userID          | INT         | Foreign Key (User)             |
|            | resourceID      | INT         | Foreign Key (Resource)         |
|            | borrowDate      | DATE        | Not Null                       |
|            | returnDate      | DATE        |                                |
|            | dueDate         | DATE        | Not Null                       |
|            | lateFee         | DECIMAL     | Calculated on overdue returns  |
| **Author** | authorID        | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | biography       | TEXT        |                                |
| **Publisher** | publisherID  | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | address         | VARCHAR     |                                |

### Determine Primary Keys
Each relation has a unique primary key to identify each tuple in the relation:
- **User:** `userID`
- **Resource:** `resourceID`
- **Borrowing:** `borrowID`
- **Author:** `authorID`
- **Publisher:** `publisherID`

### Establish Foreign Keys
To maintain referential integrity, foreign key constraints are applied in the corresponding relations:
- **User.userID** is a foreign key in the **Borrowing** relation.
- **Resource.resourceID** is a foreign key in the **Borrowing** relation.
- **Author.authorID** is a foreign key in the **Resource** relation.
- **Publisher.publisherID** is a foreign key in the **Resource** relation.

---

## 3. Schema Documentation

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

---

## 4. Generate DDL

Based on the relational schema, SQL DDL statements are prepared to create tables in the database:

```sql
CREATE TABLE User (
    userID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Member') NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE Author (
    authorID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE Publisher (
    publisherID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255)
);

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

CREATE TABLE Borrowing (
    borrowID INT PRIMARY KEY,
    userID INT NOT NULL,
    resourceID INT NOT NULL,
    borrowDate DATE NOT NULL,
    returnDate DATE,
    dueDate DATE NOT NULL,
    lateFee DECIMAL(10, 2),
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (resourceID) REFERENCES Resource(resourceID)
);
```

The DDL statements above will create the database schema, defining tables, attributes, data types, primary keys, and foreign keys.

---

## 5. Normalization Considerations

While this schema adheres to basic design principles, future refinement through normalization (e.g., BCNF or 3NF) may be needed to minimize data redundancy and improve data integrity.

---

## 6. Appendices

Additional design decisions and assumptions include:
- **Data Type Selection:** VARCHAR is used for flexible text fields, ENUM for limited choices (e.g., role and resource type).
- **Late Fee Calculation:** Assumes late fees are stored as a decimal, to allow flexibility in calculating and updating fees as needed.

---

## 7. GitHub Repository Management

All project artifacts are maintained in the GitHub repository. The team leader will submit the repository URL for this project part on Canvas.
