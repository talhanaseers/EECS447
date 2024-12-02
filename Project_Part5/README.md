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

---

## **Folder Structure**
```
Project_Part5
├── DDL/                          # SQL scripts for schema creation and constraints
│   ├── create_tables.sql         # Script for creating tables
│   ├── insert_data.sql           # Script for populating tables with initial data
│   └── constraints.sql           # Script for adding constraints
├── Data/                         # Sample datasets used for testing
│   ├── sample_data.csv           # Sample data for resources
│   ├── member_data.csv           # Sample data for members
│   ├── resource_data.csv         # Sample data for library resources
│   └── borrowing_data.csv        # Sample data for borrowing transactions
├── Documentation/                # Project documentation and resources
│   ├── Relational_Schema_Diagram.png # Visual representation of the database schema
│   ├── final_report.md           # Final project report
│   ├── requirements.md           # Project requirements and objectives
│   ├── setup_guide.md            # Instructions for setting up the database
│   ├── testing_report.md         # Testing procedures and results
│   └── data_dictionary.md        # Detailed description of database entities and attributes
├── Queries/                      # SQL queries for reporting and analysis
│   ├── borrowing_history.sql     # Query to track borrowing history
│   ├── late_fees.sql             # Query to calculate late fees
│   └── resource_availability.sql # Query for checking resource availability
└── README.md                     # Main project documentation file
```

---

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
- A relational database management system (MySQL).
- Basic knowledge of SQL.

### Setup Instructions
1. Clone this repository:  
   ```bash
   git clone https://github.com/talhanaseers/EECS447/Project_Part5.git
