## Data Definition Language

SQL DDL statements are prepared to create tables in the database, based on the relational schema:

```sql
CREATE TABLE User (
    userID INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role ENUM('Admin', 'Member') NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    status ENUM('Active', 'Expired', 'Suspended') NOT NULL,
    membershipValidUntil DATE
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

CREATE TABLE FeePolicy (
    policyID INT PRIMARY KEY,
    role ENUM('Admin', 'Member') NOT NULL,
    baseFee DECIMAL(10, 2) NOT NULL,
    maxFee DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ResourceType (
    typeID INT PRIMARY KEY,
    typeName ENUM('Book', 'Magazine', 'Digital Media') NOT NULL
);

CREATE TABLE Resource (
    resourceID INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    typeID INT NOT NULL,
    authorID INT,
    publisherID INT,
    availableCopies INT NOT NULL,
    totalCopies INT NOT NULL,
    FOREIGN KEY (typeID) REFERENCES ResourceType(typeID),
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
    policyID INT NOT NULL,
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (resourceID) REFERENCES Resource(resourceID),
    FOREIGN KEY (policyID) REFERENCES FeePolicy(policyID)
);

```

The DDL statements above will create the database schema, defining tables, attributes, data types, primary keys, and foreign keys.
