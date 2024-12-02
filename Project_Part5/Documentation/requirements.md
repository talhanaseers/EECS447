# Project Requirements - Library Management System Database

## Overview

The **Library Management System (LMS)** database is designed to streamline the management of library resources, memberships, and borrowing activities. This project involves creating a relational database system that captures essential entities and relationships necessary for day-to-day library operations. The system should also maintain data integrity, allow for role-based access, and be scalable for future enhancements.

## Functional Requirements

### 1. User Management
- The system should support two types of users:
  - **Members**: Can borrow resources, return them, and view their borrowing history.
  - **Administrators**: Can manage resources, view user activity, and update library data.
  
### 2. Resource Management
- The database should maintain records of various resources such as:
  - **Books**
  - **Magazines**
  - **Digital Media**
- Each resource should have attributes such as:
  - Title
  - Author(s)
  - Publisher
  - Resource type (e.g., Book, Magazine)
  - Availability status (e.g., Available, Borrowed)
  
### 3. Borrowing and Returning System
- Members should be able to borrow and return resources.
- The system should log each borrowing transaction and track due dates.
- Late fees should be calculated automatically when a resource is returned late.

### 4. Fee Management
- The system should calculate late fees based on:
  - The type of resource (e.g., book, magazine)
  - The length of time the resource is overdue.
- Late fees should be charged to the member’s account and tracked until payment is made.

### 5. Reporting
- The system should support SQL queries to generate reports, including:
  - **Borrowing History**: A list of borrowed resources by a member.
  - **Late Fees**: A report of late fees owed by members.
  - **Most Borrowed Books**: A list of the most popular resources in the library.
  - **User Activity Report**: A summary of a member’s borrowing activity.

### 6. Data Integrity and Constraints
- The database must enforce the following constraints:
  - **Primary Keys**: For each entity (e.g., User, Resource, Borrowing, etc.).
  - **Foreign Keys**: To maintain referential integrity between related entities (e.g., a borrow record should be linked to a valid user and resource).
  - **Check Constraints**: For valid data (e.g., due dates should not be in the past).
  
## Non-Functional Requirements

### 1. **Scalability**
- The database should be designed to accommodate a growing number of resources, members, and borrowing transactions. This includes ensuring that the database can handle high concurrency, especially during peak usage times.

### 2. **Performance**
- Queries and transactions should be optimized to ensure efficient performance, even with large datasets.
- Indexing should be used for frequently accessed attributes (e.g., user IDs, resource IDs).

### 3. **Security**
- The system should implement role-based access controls to ensure that users have appropriate permissions based on their roles (e.g., Members vs. Administrators).
  
### 4. **Backup and Recovery**
- The database should have a reliable backup and recovery mechanism to prevent data loss in case of a failure.

## Technical Requirements

### 1. **Database Platform**
- The system will be built on a **relational database management system (RDBMS)**, such as MySQL, PostgreSQL, or SQL Server.

### 2. **SQL Features**
- The database will utilize advanced SQL features such as:
  - **Triggers**: For automatic late fee calculations.
  - **Stored Procedures**: To manage complex operations like borrowing and returning resources.
  - **Views**: To simplify access to frequently queried data.

### 3. **Normalization**
- The database will adhere to **Third Normal Form (3NF)** to eliminate redundancy and ensure data integrity.

## Future Enhancements

### 1. **Advanced Reporting**
- Generate detailed reports on borrowing trends, resource utilization, and member activity.

### 2. **Integration with Mobile Applications**
- Extend access to the system via mobile platforms to enhance user convenience.

### 3. **Recommendation System**
- Implement a recommendation engine that suggests resources based on user activity and borrowing history.

## Deliverables

1. **Relational Database Schema**: Detailed schema diagram and SQL scripts for creating tables, constraints, triggers, and views.
2. **Sample Data**: CSV files containing sample data for testing the database.
3. **Queries**: SQL queries to generate reports and perform analytics.
4. **Project Documentation**: Comprehensive documentation detailing the database design, setup instructions, and testing results.

---

## References

- **Eloquent JavaScript**: For database design principles.
- **SQL Documentation**: For advanced SQL features and functions.


