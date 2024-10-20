# ER Diagram Documentation for Library Management System

## 1. Introduction

### Project Overview
The Library Management System database is designed to efficiently manage a library's inventory, including books, digital media, and magazines, while tracking client memberships and borrowing activities. The system facilitates the availability of resources, borrowing rules, and calculates late fees. It also supports generating reports for administrators to monitor the library's usage and resources. The database ensures smooth multi-user interaction through transaction management and role-based access control, aligning with the system's goal of improving library operations and user satisfaction.


### Scope
The project will focus on developing a relational database that supports core library functions, such as resource management, user management, and borrowing operations. It will enforce borrowing limits, track overdue items, and apply late fees. Additionally, it will include transaction management and role-based access for different user types (Admins, Members). However, the system will exclude any non-library-related services, such as financial transactions outside of library fees, and will not support resources unrelated to the library's collection.

### Glossary
- **Library Resource:** Any item available for borrowing, including books, digital media, and magazines.
- **Borrowing Rules:** Constraints on the number of items a user can borrow and the duration for which they can be borrowed.
- **Late Fees:** Fines imposed on overdue borrowed items.
- **User Role:** Specific access level assigned to a user (e.g., Admin, Member).
- **Transaction Management:** Ensuring reliable application of all database changes in multi-user scenarios.
- **Admin Users:** Users responsible for managing library resources, user accounts, and generating reports.
- **Member Users:** End-users who borrow and return resources, manage accounts, and pay any overdue fees.
- **Resource:** An item in the library collection, such as a book, magazine, or digital media.


---

## 2. Review Requirements

The following entities, attributes, and relationships are established based on the previously documented requirements in database_requirements.md:

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

## 3. ER Model

**Major Entities:**
- User
- Resource
- Borrowing
- Author
- Publisher

**Example Attributes:**
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


