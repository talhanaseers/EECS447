# Final Report: Library Management System Database

## Course Information
- **Course**: EECS 447 - Database Systems  
- **Instructor**: Professor Dr. Hossein Saidian  
- **Semester**: Fall 2024
- **Submission Data**: December 3, 2024


## Team Information
- **Team Name**: Library Innovators  
- **Team Members**:  
  - Talha Naseer (Team Administrator)  
  -  

---

## Table of Contents
1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Database Design](#database-design)
4. [Implementation Highlights](#implementation-highlights)
5. [Challenges and Solutions](#challenges-and-solutions)
6. [Future Enhancements](#future-enhancements)
7. [Progress Log](#progress-log)
8. [Folder Structure](#folder-structure)
9. [Conclusion](#conclusion)

---

## Introduction

The **Library Management System (LMS)** database project aims to simplify and enhance library operations by providing a structured, relational database system. The design ensures robust management of library resources, user memberships, borrowing activities, and late fee policies. The database adheres to normalization principles, ensuring data integrity and scalability for multi-user environments.

---

## Objectives

- **Streamline Operations**: Efficiently manage library resources, borrowing, and returning activities.
- **Enhance Data Integrity**: Enforce constraints like primary and foreign keys for consistency.
- **Scalability**: Design the schema to accommodate future features like reporting and analytics.
- **Role-Based Access**: Differentiate functionalities for administrators and members.

---

## Database Design

### Relational Schema
The relational schema was designed to capture core entities such as:
- **User**: Tracks details about library members and staff.
- **Resource**: Manages books, magazines, and digital media inventory.
- **Borrowing**: Logs borrowing and returning activities.
- **Author**: Stores author information linked to resources.
- **Publisher**: Manages publisher details.
- **FeePolicy**: Implements role-based late fee calculations.
- **ResourceType**: Categorizes resources into predefined types.

### Normalization
- The schema adheres to **Third Normal Form (3NF)** to eliminate redundancy and ensure dependencies are properly organized.

---

## Implementation Highlights

- **Constraints**:
  - Primary Keys: Ensure unique identification for all entities.
  - Foreign Keys: Maintain relationships between entities, ensuring referential integrity.
- **Testing**:
  - Conducted edge-case testing for borrowing transactions and late fee calculations.
  - Verified referential integrity through simulated operations.

### Key SQL Features
- **Triggers**: Automate fee calculations for late returns.
- **Views**: Simplify access to frequently queried data.
- **Stored Procedures**: Manage complex operations like borrowing and returning.

---

## Challenges and Solutions

### Challenge: Maintaining Data Integrity
- **Solution**: Implemented strict constraints and transaction controls to prevent invalid data.

### Challenge: Scalability for Multi-User Environments
- **Solution**: Optimized the schema with indexing and normalization to support high-concurrency access.

---

## Future Enhancements

1. **Advanced Reporting**: Generate detailed analytics on borrowing trends and resource utilization.
2. **Integration with Mobile Apps**: Enable seamless access through mobile platforms.
3. **Recommendation System**: Suggest resources based on user borrowing history.

---

## **Progress Log**

| **Date**       | **Tasks Completed**                                                                 | **Decisions/Changes/Notes**                                                                                   |
|-----------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Nov 28, 2024**| Finalized the database schema and began ER diagram creation.                        | No changes made to initial plan.                                                                       |
| **Nov 29, 2024**| Converted the ER diagram into relational schema and started writing SQL scripts.    | Adjusted cardinalities for `Borrowing` relation to accommodate multiple borrow-return cycles.           |
| **Nov 30, 2024**| Tested SQL scripts for schema creation and data insertion.                         | Added additional constraints for late fee calculations.                                                |
| **Dec 1, 2024** | Created documentation for schema and setup instructions.                           | Clarified relationships in `ResourceType` table for better granularity.                                |
| **Dec 2, 2024** | Finalized and reviewed documentation, relational schema, and test queries.          | No major changes.                                                                                      |
| **Dec 3, 2024** |  |   

---

## **Folder Structure**

Project_Part5
├── DDL/                          # SQL scripts for schema creation and constraints
│   ├── create_tables.sql         # Script for creating tables
│   ├── insert_data.sql           # Script for populating tables with initial data
│   ├── constraints.sql           # Script for adding constraints
│   ├── triggers.sql              # Script for creating triggers
│   └── views.sql                 # Script for creating views
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
│   ├── most_borrowed_books.sql   # Query to find the most borrowed books
│   ├── user_activity_report.sql  # Query for generating user activity reports
│   └── resource_availability.sql # Query for checking resource availability
└── README.md                     # Main project documentation file


---

## Conclusion

The Library Management System Database achieves its objective of simplifying library operations while ensuring robust data integrity and scalability. By adhering to industry-standard design principles and employing rigorous testing, this project provides a reliable foundation for future enhancements like analytics and mobile integration.

This database not only fulfills current library needs but also anticipates future demands, ensuring long-term usability and adaptability.
