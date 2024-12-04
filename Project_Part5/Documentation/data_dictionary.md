### Data Dictionary

The data dictionary documents each relation, its attributes, data types, domains, and constraints, providing a clear reference for developers.

| Relation        | Attribute            | Data Type                        | Domain                                        | Constraint                                    |
|-----------------|----------------------|----------------------------------|-----------------------------------------------|-----------------------------------------------|
| **User**        | userID               | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **User**        | name                 | VARCHAR                          | String (1 to 100 characters)                  | Not Null                                      |
| **User**        | role                 | ENUM                             | {'Admin', 'Member'}                           | Not Null                                      |
| **User**        | email                | VARCHAR                          | Valid email format                            | Unique, Not Null                              |
| **User**        | phone                | VARCHAR                          | String (0 to 15 characters)                   | Optional                                      |
| **User**        | membershipStatus     | ENUM                             | {'Active', 'Expired', 'Suspended'}            | Not Null                                      |
| **User**        | validUntil           | DATE                             | Valid date                                    | Not Null                                      |
| **Resource**    | resourceID           | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **Resource**    | title                | VARCHAR                          | String (1 to 200 characters)                  | Not Null                                      |
| **Resource**    | type                 | ENUM                             | {'Book', 'Magazine', 'Digital Media'}         | Not Null                                      |
| **Resource**    | authorID             | INT                              | Positive integer (exists in Author table)     | Foreign Key (Author.authorID), Not Null       |
| **Resource**    | publisherID          | INT                              | Positive integer (exists in Publisher table)  | Foreign Key (Publisher.publisherID), Not Null |
| **Resource**    | availableCopies      | INT                              | Non-negative integer                          | Not Null                                      |
| **Resource**    | totalCopies          | INT                              | Non-negative integer, >= availableCopies      | Not Null                                      |
| **Borrowing**   | borrowID             | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **Borrowing**   | userID               | INT                              | Positive integer (exists in User table)       | Foreign Key (User.userID), Not Null           |
| **Borrowing**   | resourceID           | INT                              | Positive integer (exists in Resource table)   | Foreign Key (Resource.resourceID), Not Null   |
| **Borrowing**   | borrowDate           | DATE                             | Valid date                                    | Not Null                                      |
| **Borrowing**   | returnDate           | DATE                             | Valid date or NULL                            | Optional                                      |
| **Borrowing**   | dueDate              | DATE                             | Valid date                                    | Not Null                                      |
| **Borrowing**   | lateFee              | DECIMAL                          | Positive decimal number                       | Calculated                                    |
| **Author**      | authorID             | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **Author**      | name                 | VARCHAR                          | String (1 to 100 characters)                  | Not Null                                      |
| **Author**      | biography            | TEXT                             | String (up to 5000 characters)                | Optional                                      |
| **Publisher**   | publisherID          | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **Publisher**   | name                 | VARCHAR                          | String (1 to 100 characters)                  | Not Null                                      |
| **Publisher**   | address              | VARCHAR                          | String (1 to 255 characters)                  | Optional                                      |
| **FeePolicy**   | policyID             | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **FeePolicy**   | role                 | ENUM                             | {'Admin', 'Member'}                           | Not Null                                      |
| **FeePolicy**   | baseFee              | DECIMAL                          | Positive decimal number                       | Not Null                                      |
| **FeePolicy**   | maxFee               | DECIMAL                          | Positive decimal number                       | Not Null                                      |
| **ResourceType**| resourceTypeID       | INT                              | Positive integer                              | Primary Key, Unique, Not Null                 |
| **ResourceType**| typeName             | ENUM                             | {'Book', 'Magazine', 'Digital'}               | Not Null                                      |

