# ER Diagram Documentation for Library Management System

## 1. Introduction

### Project Overview
The Library Management System (LMS) database is designed to effectively manage the library's inventory of books, digital media, and magazines while also overseeing client memberships and borrowing activities. It enables efficient tracking of item availability, enforcement of borrowing limits, late fee calculation, and comprehensive reporting functionalities.

### Scope
This project encompasses the development of a relational database capable of supporting multi-user operations, transaction management, and role-based access control. It will not address non-library-related resources or financial services beyond the scope of library fees.

### Glossary
- **Library Resource:** Any item (book, digital media, magazine) available for borrowing.
- **Borrowing Rules:** Constraints on the number of items a user can borrow and the duration for which they can be borrowed.
- **Late Fees:** Fines imposed on overdue borrowed items.
- **User Role:** Specific access level assigned to a user (e.g., Admin, Member).
- **Transaction Management:** Ensuring reliable application of all database changes in multi-user scenarios.

---

## 2. Review Requirements

The following entities, attributes, and relationships are established based on the previously documented requirements:

### Entities and Attributes
1. **User**
   - **Attributes:** 
     - userID (int, Primary Key)
     - name (varchar)
     - role (enum: 'Admin', 'Member')
     - email (varchar)
     - phone (varchar)
   
2. **Resource**
   - **Attributes:** 
     - resourceID (int, Primary Key)
     - title (varchar)
     - type (enum: 'Book', 'Magazine', 'Digital Media')
     - author (varchar)
     - availableCopies (int)
     - totalCopies (int)
   
3. **Borrowing**
   - **Attributes:** 
     - borrowID (int, Primary Key)
     - userID (int, Foreign Key)
     - resourceID (int, Foreign Key)
     - borrowDate (date)
     - returnDate (date)
     - dueDate (date)
     - lateFee (decimal)

### Relationships
- **User to Borrowing:** One-to-Many (1..N) - A user can borrow multiple resources.
- **Resource to Borrowing:** One-to-Many (1..N) - A resource can be borrowed multiple times by different users.

---

## 3. Validate Your Model

### Get Ready for ER Modeling

#### Identify Entities
List all the major entities that will be part of your database. This includes the initial entities in the project description, the ones you identified during the requirements engineering, and the additional ones during your team brainstorming.

**Major Entities:**
- User
- Resource
- Borrowing
- Author
- Publisher

#### Define Attributes
For each entity, list its attributes and specify the data types or constraints.

**Example:**
- **User**
  - userID (int, Primary Key)
  - name (varchar, Not Null)
  - role (enum: 'Admin', 'Member', Not Null)
  - email (varchar, Unique, Not Null)
  - phone (varchar)

- **Resource**
  - resourceID (int, Primary Key)
  - title (varchar, Not Null)
  - type (enum: 'Book', 'Magazine', 'Digital Media', Not Null)
  - authorID (int, Foreign Key, Not Null)
  - publisherID (int, Foreign Key, Not Null)
  - availableCopies (int, Not Null)
  - totalCopies (int, Not Null)

- **Borrowing**
  - borrowID (int, Primary Key)
  - userID (int, Foreign Key, Not Null)
  - resourceID (int, Foreign Key, Not Null)
  - borrowDate (date, Not Null)
  - returnDate (date)
  - dueDate (date, Not Null)
  - lateFee (decimal)

#### Establish Relationships
Determine how the entities are related to each other. Define the cardinality (one-to-one, one-to-many, many-to-many) and any constraints.

**Example Relationships:**
- **User to Borrowing:** One-to-Many (1..N) - A user can borrow multiple resources.
- **Resource to Borrowing:** One-to-Many (1..N) - A resource can be borrowed multiple times by different users.
- **Resource to Author:** Many-to-One (N..1) - A resource can have one author, but an author can write multiple resources.
- **Resource to Publisher:** Many-to-One (N..1) - A resource can be published by one publisher, but a publisher can publish multiple resources.

---

## 4. Appendices

- **Design Choices:** 
  - The entities were chosen based on the core functions of the library management system, focusing on user management, resource tracking, and borrowing management.
- **Assumptions:** 
  - It is assumed that users will have distinct roles affecting their permissions within the system.
- **Additional Notes:** 
  - Any updates or revisions will be documented in future versions.

---

## 5. GitHub Repository Management

Continue to manage all project artifacts in the GitHub repository. The team leader will submit the repository URL containing this documentation.
