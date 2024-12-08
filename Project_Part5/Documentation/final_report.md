# Final Report: Library Management System Database

## Course Information
- **Course**: EECS 447 - Database Systems  
- **Instructor**: Professor Dr. Hossein Saidian  
- **Semester**: Fall 2024
- **Submission Data**: December 3, 2024


## Team Information
****Team Name****: Library Innovators  
#### Team Members:  
  - **Project Leader:** Alec Slavik
  - **Team Adminstrator:** Talha Naseer
  - **Assistant Team Adminstrator:** Deborah Onuosa
  - **Assistant Project Leader:** Muhammad Abdullah
  - **Technical Leader:** Conner Glazner
  - **Data Adminstrator:** Atharva Patil

### Responsibilities Assigned for Project Part 5:
- **Talha Naseer**: Choosing platform, filling any gaps in any task/roles, submission
- **Deborah Onuosa**: Documentation
- **Atharva Patil**: Creating database
- **Conner Glazner**: Functionality testing 
- **Muhammad Abdullah**: Test and validate 
- **Alec Slavik**: Data population

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
**Refer to Documentation.pdf for detailed overview**

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

### Refer to Documentation.pdf for detailed progress tracking

| **Date**       | **Tasks Completed**                                                                 | **Decisions/Changes/Notes**                                                                                   |
|-----------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Nov 28, 2024**| Finalized the database schema and began ER diagram creation.                        | No changes made to initial plan.                                                                       |
| **Nov 29, 2024**| Converted the ER diagram into relational schema and started writing SQL scripts.    | Adjusted cardinalities for `Borrowing` relation to accommodate multiple borrow-return cycles.           |
| **Nov 30, 2024**| Tested SQL scripts for schema creation and data insertion.                         | Added additional constraints for late fee calculations.                                                |
| **Dec 1, 2024** | Created documentation for schema and setup instructions.                           | Clarified relationships in `ResourceType` table for better granularity.                                |
| **Dec 2, 2024** | Finalized and reviewed documentation, relational schema, and test queries.          | No major changes.                                                                                      |
| **Dec 3, 2024** | Organized files and folders, submission to canvas. | No changes.   
| **Dec 7, 2024** | SQL Report & Additional Queries added as per new assignment | New Repositories for additional assignments   
| **Dec 8, 2024** | Finalized changes, resubmission for additional tasks | No changes.   

---

## **Folder Structure**
```
Project_Part5
│
├── Additional Queries (Assigned December 5)/       # Additional SQL Queries (Alternative to live team demos — Assigned December 5, 2024)
│   ├── Fine_Calculation.sql                        # Additional SQL Query
│   ├── Book_Availability.sql                       # Additional SQL Query
│   ├── Frequent_Borrowers_of_a_Specific_Genre.sql  # Additional SQL Query
│   ├── Books_Due_Soon.sql                          # Additional SQL Query
│   ├── Members_with_Overdue_Books.sql              # Additional SQL Query
│   ├── Average_Borrowing_Time.sql                  # Additional SQL Query
│   └── Most_Popular_Author_in_the_Last_Month.sql   # Additional SQL Query
│
├── SQL Report (Assigned December 5)/               # SQL Report and Output Screenshot (Alternative to live team demos — Assigned December 5, 2024)
│   ├── Operational_Efficiency_Report.md            # Operational Efficiency Report Assigned 
│   └── Output_Screenshot.png                       # Screenshot of Output
│
├── DDL/                                # SQL scripts for schema creation and constraints
│   ├── create_tables.sql               # Script for creating tables
│   ├── insert_data.sql                 # Script for populating tables with initial data
│   └── constraints.sql                 # Script for adding constraints
│
├── Data/                               # Sample datasets used for testing
│   ├── Data Files/                     # Data File for data poplation
│   │     ├── author_data.sql           # SQL Scripts to populate author data
│   │     ├── borrowing_data.sql        # SQL Scripts to populate borrowing data
│   │     ├── fee_policy_data.sql       # SQL Scripts to populate fee policy data
│   │     ├── publishers_data.sql       # SQL Scripts to populate publishers data
│   │     ├── resource_data.sql         # SQL Scripts to populate resource data
│   │     └── user_data.sql             # SQL Scripts to populate user data
│   │
│   ├── Scripts/                               # Python Scripts to generate data
│   │     ├── author_data_generator.py         # Python Scripts to generate author data
│   │     ├── borrowing_data_generator.py      # Python Scripts to generate borrowing data
│   │     ├── fee_policy_data_generator.py     # Python Scripts to generate fee policy data
│   │     ├── publishers_data_generator.py     # Python Scripts to generate publishers data
│   │     ├── resource_data_generator.py       # Python Scripts to generate resource data
│   │     └── user_data_generator.py           # Python Scripts to generate user data
│   │
│   └── sample_data.csv                  # Sample data for resources
│
├── Documentation/                       # Project documentation and resources
│   ├── Relational_Schema_Diagram.png    # Visual representation of the database schema
│   ├── final_report.md                  # Final project detailed report
│   ├── Documentation.pdf                # Detailed documentation
│   ├── requirements.md                  # Project requirements and objectives
│   ├── setup_guide.md                   # Instructions for setting up the database
│   ├── testing_report.md                # Testing procedures and results
│   └── data_dictionary.md               # Detailed description of database entities and attributes
│   
├── Queries/                                       # SQL queries
│   ├── Borrowing_Management/                      # Queries to manage borrowing 
│   │    ├── apply_late_fees.sql                   # Queries for applying late fees
│   │    ├── checkout_resource.sql                 # Queries for checking out resources
│   │    └── return_resource.sql                   # Queries for returning resources
│   │
│   ├── Resource_Management/                       # Queries to manage resoources
│   │    ├── add_new_resource.sql                  # Queries for adding new resources
│   │    ├── remove_resource.sql                   # Queries for removing resources
│   │    └── update_avaialble_copies.sql           # Queries for updating avaialble copies
│   │
│   ├── User_Management/                           # Queries to manage users
│   │    ├── add_user.sql                          # Queries to add users
│   │    ├── delete_user.sql                       # Queries to delete users
│   │    └── set_user_role.sql                     # Queries to set user roles
│   │
│   └── Search_and_Reports/                        # Queries to manage searches and reports
│        ├── overdue_items_report.sql              # Queries for over due items report
│        ├── resource_availability_report.sql      # Queries for resource availability report
│        ├── resource_usage_report.sql             # Queries for usage report
│        ├── top_ten_borrowed_resources_report.sql # Queries for top ten borrowed report
│        └── user_borrowing_history_report.sql     # Queries for user borrowing history report
│
└── README.md             # Entry Point Documentation (Refer to Documentation.pdf for detailed documentation, final_report.md for a
                            detailed final report)
```

---

## Conclusion

The Library Management System Database achieves its objective of simplifying library operations while ensuring robust data integrity and scalability. By adhering to industry-standard design principles and employing rigorous testing, this project provides a reliable foundation for future enhancements like analytics and mobile integration.

This database not only fulfills current library needs but also anticipates future demands, ensuring long-term usability and adaptability.



**Refer to Documentation.pdf for detailed progress log, and enhanced details relevant to project part 5.**

**Refer to testing_report.md for detailed testing procedures and summaries.**
