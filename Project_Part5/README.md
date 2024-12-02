# Library Management System (LMS)

## Overview
The Library Management System (LMS) database is a relational structure designed to streamline library operations, ensuring efficient management of resources, user memberships, borrowing activities, and late fees. By incorporating robust database design principles, the LMS guarantees data integrity, scalability, and multi-user functionality, making it an ideal solution for both small and large libraries.

## Features
- **User Management**  
  Maintain detailed records of users, including roles (e.g., Admin, Member) and membership statuses.

- **Resource Inventory**  
  Track books, magazines, and digital media with real-time data on availability and total copies.

- **Borrowing System**  
  Log borrowing and return activities, enforce due dates, and calculate late fees based on role-specific policies.

- **Data Integrity**  
  Use primary keys, foreign keys, and domain constraints to maintain referential consistency and prevent data anomalies.

- **Role-Based Fee Policies**  
  Differentiate borrowing rules and late fee structures for admins and members.

## Technical Highlights
### Schema Design
The LMS schema adheres to Third Normal Form (3NF) to ensure minimal redundancy and optimal performance. It includes the following core entities:
- **User**: Tracks library members and staff.
- **Resource**: Manages inventory, categorized by resource type.
- **Borrowing**: Logs transactions for tracking resource utilization.
- **Author**: Maintains information on resource creators.
- **Publisher**: Tracks publishers associated with resources.
- **FeePolicy**: Implements late fee rules based on user roles.
- **ResourceType**: Defines types of resources available.

### Integrity Constraints
- **Primary Keys**: Ensure unique identification of records.
- **Foreign Keys**: Enforce relationships between tables (e.g., `Borrowing.userID` → `User.userID`).
- **Domain Constraints**: Restrict attribute values to valid ranges or enumerations.

### Scalability
The schema is designed to accommodate future enhancements, such as:
- Integration with mobile apps.
- Advanced reporting features.
- Personalized resource recommendations based on borrowing history.

## Installation
### Prerequisites
- A relational database management system (PostgreSQL).
- Basic knowledge of SQL.

### Setup Instructions
1. Clone this repository:  
   ```bash
   git clone https://github.com/talhanaseers/EECS447.git
