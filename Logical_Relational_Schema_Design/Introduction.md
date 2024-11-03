## Introduction

### Project Overview
The Library Management System database serves as the backbone for managing various resources within the library, supporting inventory tracking for books, digital media, and magazines. The system manages user roles and borrowing activities, applying late fees where necessary and enabling administrative oversight. With multi-user capabilities, role-based access, and transaction management, this database supports efficient and reliable library operations, aligning with the library’s goal to enhance user engagement and streamline administrative processes.

### Scope
This project segment focuses on converting the conceptual ER model into a robust relational schema. This schema emphasizes data integrity, ensuring each library function, such as resource tracking, user management, and borrowing activities, is supported by primary and foreign key constraints. Key operations include borrowing, returning, and applying late fees for overdue items, with transaction management for smooth multi-user interaction. Exclusions include unrelated services, such as non-library-related financial transactions.

### Glossary
- **Relational Schema:** The structured outline for database tables, detailing each table’s attributes, primary keys, and foreign keys.
- **Primary Key (PK):** A unique identifier for records within a table, ensuring data uniqueness and enabling efficient data retrieval. Example: userID in the User table.
- **Foreign Key (FK):** An attribute in one table that references the primary key in another table, establishing relationships and ensuring referential integrity.
- **Entity:** A core object or concept within the database, representing real-world elements like User, Resource, or Author.
- **Attribute:** A property or characteristic of an entity, such as name or email for a User.
- **Domain:** The set of valid values for an attribute, such as integers for userID or a list of roles (Admin, Member) for role.
- **Relationship:** The connection between two entities, such as User to Borrowing, represented through foreign keys.
- **Referential Integrity:** A rule ensuring foreign keys accurately reference valid primary key values, preventing orphaned records.
- **Normalization:** Organizing data to reduce redundancy and improve integrity by dividing data into related tables, often to achieve 3NF or BCNF.
- **Data Dictionary:** A document outlining each table’s attributes, their data types, constraints, and descriptions, providing a reference for database design.
- **Transaction Management:** Ensures all transactions are processed correctly in a multi-user environment, maintaining data consistency.
- **Role-Based Access Control (RBAC):** Restricts user permissions based on assigned roles, such as Admin or Member.
- **Constraint:** A rule applied to table attributes, such as NOT NULL or UNIQUE, to enforce data integrity.


