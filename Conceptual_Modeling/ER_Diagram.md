# ER Diagram Documentation for Library Management System

## 1. Introduction

### Project Overview
The Library Management System database is designed to efficiently manage a library's inventory, including books, digital media, and magazines, while tracking client memberships and borrowing activities. The system facilitates the availability of resources, borrowing rules, and calculates late fees. It also supports generating reports for administrators to monitor the library's usage and resources. The database ensures smooth multi-user interaction through transaction management and role-based access control, aligning with the system's goal of improving library operations and user satisfaction.

### Scope
The project will focus on developing a relational database that supports core library functions, such as resource management, user management, and borrowing operations. It will enforce borrowing limits, track overdue items, and apply late fees. Additionally, it will include transaction management and role-based access for different user types (Admins, Members). However, the system will exclude any non-library-related services, such as financial transactions outside of library fees, and will not support resources unrelated to the library's collection.

### Glossary
- **Library Resource:** Any item available for borrowing, including books, digital media, and magazines.
- **Borrowing Rules:** Constraints on the number of items a user can borrow and the duration for which they can be borrowed.
- **Late Fees:** Fines imposed on overdue borrowed items, based on a set **FeePolicy**.
- **FeePolicy:** Defines the rules for calculating late fees, including rates and conditions.
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
     - name (varchar, Not Null)
     - role (enum: 'Admin', 'Member', Not Null)
     - email (varchar, Unique, Not Null)
     - phone (varchar)
     - status (enum: 'Active', 'Suspended') — Indicates if the user is in good standing
     - membershipValidUntil (date) — Expiry date for the user's membership validity

2. **Resource**
   - **Attributes:** 
     - resourceID (int, Primary Key)
     - title (varchar, Not Null)
     - typeID (int, Foreign Key, Not Null) — Links to **ResourceType** entity
     - authorID (int, Foreign Key, Not Null)
     - publisherID (int, Foreign Key, Not Null)
     - availableCopies (int, Not Null)
     - totalCopies (int, Not Null)

3. **ResourceType**
   - **Attributes:**
     - typeID (int, Primary Key)
     - typeName (enum: 'Book', 'Magazine', 'Digital Media', Not Null) — Indicates the type of resource

4. **Borrowing**
   - **Attributes:** 
     - borrowID (int, Primary Key)
     - userID (int, Foreign Key, Not Null)
     - resourceID (int, Foreign Key, Not Null)
     - borrowDate (date, Not Null)
     - returnDate (date)
     - dueDate (date, Not Null)
     - lateFee (decimal) — Applied based on **FeePolicy**

5. **FeePolicy**
   - **Attributes:** 
     - policyID (int, Primary Key)
     - rate (decimal, Not Null) — Rate per day for overdue items
     - gracePeriod (int) — Days allowed before late fees start applying
     - maxFee (decimal) — Maximum late fee chargeable for a single item

6. **Author**
   - **Attributes:** 
     - authorID (int, Primary Key)
     - name (varchar, Not Null)
     - biography (text)

7. **Publisher**
   - **Attributes:** 
     - publisherID (int, Primary Key)
     - name (varchar, Not Null)
     - address (varchar)

### Relationships

- **User to Borrowing:** 
   - One-to-Many (1..N) - A user can borrow multiple resources.

- **ResourceType to Resource:** 
   - One-to-Many (1..N) - Each **ResourceType** can relate to multiple resources, but each resource has only one type.

- **Resource to Borrowing:** 
   - One-to-Many (1..N) - A resource can be borrowed multiple times by different users.

- **Resource to Author:** 
   - Many-to-One (N..1) - A resource can have one author, but an author can write multiple resources.

- **Resource to Publisher:** 
   - Many-to-One (N..1) - A resource can be published by one publisher, but a publisher can publish multiple resources.

- **FeePolicy to Borrowing:** 
   - One-to-Many (1..N) - Each borrowing entry follows a fee policy for late fee calculation.

---

## 3. ER Model

**Major Entities:**
- User
- Resource
- ResourceType
- Borrowing
- FeePolicy
- Author
- Publisher

**Example Attributes:**

1. **User**
   - userID (int, Primary Key)
   - name (varchar, Not Null)
   - role (enum: 'Admin', 'Member', Not Null)
   - email (varchar, Unique, Not Null)
   - phone (varchar)
   - status (enum: 'Active', 'Suspended')
   - membershipValidUntil (date)

2. **Resource**
   - resourceID (int, Primary Key)
   - title (varchar, Not Null)
   - typeID (int, Foreign Key, Not Null)
   - authorID (int, Foreign Key, Not Null)
   - publisherID (int, Foreign Key, Not Null)
   - availableCopies (int, Not Null)
   - totalCopies (int, Not Null)

3. **ResourceType**
   - typeID (int, Primary Key)
   - typeName (enum: 'Book', 'Magazine', 'Digital Media', Not Null)

4. **Borrowing**
   - borrowID (int, Primary Key)
   - userID (int, Foreign Key, Not Null)
   - resourceID (int, Foreign Key, Not Null)
   - borrowDate (date, Not Null)
   - returnDate (date)
   - dueDate (date, Not Null)
   - lateFee (decimal)

5. **FeePolicy**
   - policyID (int, Primary Key)
   - rate (decimal, Not Null)
   - gracePeriod (int)
   - maxFee (decimal)

---

**Example Relationships:**
- **User to Borrowing:** 
   - One-to-Many (1..N) - A user can borrow multiple resources.

- **ResourceType to Resource:** 
   - One-to-Many (1..N) - Each **ResourceType** can relate to multiple resources, but each resource has only one type.

- **Resource to Borrowing:** 
   - One-to-Many (1..N) - A resource can be borrowed multiple times by different users.

- **Resource to Author:** 
   - Many-to-One (N..1) - A resource can have one author, but an author can write multiple resources.

- **Resource to Publisher:** 
   - Many-to-One (N..1) - A resource can be published by one publisher, but a publisher can publish multiple resources.

- **FeePolicy to Borrowing:** 
   - One-to-Many (1..N) - Each borrowing follows a specific fee policy for late fee calculation.

---

## 4. Appendices

- **Design Choices:** 
  - The entities were chosen based on the core functions of the library management system, focusing on user management, resource tracking, and borrowing management.
  
- **Assumptions:** 
  - It is assumed that users will have distinct roles affecting their permissions within the system.
  - Late fees are applied based on a policy defined in the **FeePolicy** entity, where the rate and grace period can be adjusted.

- **Additional Notes:** 
  - **Late Fee Calculation:** Late fees are calculated based on the policy's rate and applied after the grace period if a resource is returned past its due date. The `lateFee` field in **Borrowing** records this value, and it is updated manually or by a script based on the return date.
  - **Resource Type Normalization:** The **ResourceType** entity was introduced to allow easier management of various types of library resources.
  - Any updates or revisions will be documented in future versions.
