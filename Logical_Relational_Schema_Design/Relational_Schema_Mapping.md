## Relational Schema Mapping

### Identify Relations
For each entity and relationship set in the ER diagram, a corresponding relation (table) is created:
- **User** 
- **Resource**
- **Borrowing**
- **Author**
- **Publisher**
- **FeePolicy**
- **ResourceType**


### Define Attributes and Domains
Each attribute in the entity and relationship sets is defined with a corresponding attribute in the appropriate relation, along with data types and domain constraints.

| Relation   | Attribute       | Data Type   | Domain/Constraint              |
|------------|-----------------|-------------|--------------------------------|
| **User**   | userID          | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | role            | ENUM        | ('Admin', 'Member')            |
|            | email           | VARCHAR     | Unique, Not Null               |
|            | phone           | VARCHAR     |                                |
|            | status          | ENUM        |  ('Active','Expired','Suspended')|
|            | membershipValidunti | DATE    |                                |
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
|            | policyID        | INT         | Foreign Key                    |
| **Author** | authorID        | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | biography       | TEXT        |                                |
| **Publisher** | publisherID  | INT         | Primary Key                    |
|            | name            | VARCHAR     | Not Null                       |
|            | address         | VARCHAR     |                                |
| **FeePolicy** | policyID     | INT         | Primary Key                    |
|            | role            | ENUM        | ('Admin','Member')             |
|            | baseFee         | DECIMAL     | Not Null                       |
|         | maxFee          | DECIMAL     | Maximum late fee of a single borrowing transaction|
| **ResourceType** | TypeID     | INT         | Primary Key                   |
|            | typeName         | ENUM        | ('Magazine','Digital')        |


### Determine Primary Keys
Each relation has a unique primary key to identify each tuple in the relation:
- **User:** `userID`
- **Resource:** `resourceID`
- **Borrowing:** `borrowID`
- **Author:** `authorID`
- **Publisher:** `publisherID`
- **ResourceType:** `typeID`
- **FeePolicy:** `policyID`

### Establish Foreign Keys
To maintain referential integrity, foreign key constraints are applied in the corresponding relations:
- **User.userID** is a foreign key in the **Borrowing** relation.
- **Resource.resourceID** is a foreign key in the **Borrowing** relation.
- **Author.authorID** is a foreign key in the **Resource** relation.
- **Publisher.publisherID** is a foreign key in the **Resource** relation.

