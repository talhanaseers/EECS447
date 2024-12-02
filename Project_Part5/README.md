EECS 447 Library Management System: Logical Relational Schema Design

README

Introduction
The Library Management System (LMS) database project provides a robust, relational structure to manage the library's operations. The system supports core functionalities like resource tracking, user management, borrowing activities, and late fee enforcement while ensuring data integrity and referential consistency. This database design is optimized for multi-user environments, allowing administrators to oversee operations efficiently and library members to engage seamlessly.

Project Objectives
Streamline library operations: Efficient tracking of inventory, borrowing, and returning activities.
Enhance data integrity: Establish strong primary and foreign key constraints.
Ensure role-based access: Differentiate functionalities based on user roles (e.g., Admin vs. Member).
Support scalability: Provide a robust foundation for future enhancements.
System Features
User Management: Tracks user details, roles, and membership statuses.
Resource Inventory: Manages books, magazines, and digital media, including available and total copies.
Borrowing System: Logs borrowing and returning activities, enforces due dates, and calculates late fees.
Role-Based Fee Policies: Implements fee structures specific to user roles (Admin/Member).
Data Integrity: Utilizes constraints like primary keys, foreign keys, and normalization principles to ensure consistency.
Schema Documentation
Relational Schema Diagram

The relational schema diagram visualizes the logical structure of the LMS database. It includes relations, attributes, primary keys (PKs), foreign keys (FKs), and relationships between entities.

Refer to the Relational_Schema_Diagram.png file in this repository for detailed visuals.

Data Dictionary

The data dictionary outlines the attributes, data types, domains, and constraints for each relation. View the DataDictionary.md file for a complete attribute reference.

Relations Overview

User: Manages library user details and statuses.
Resource: Tracks library inventory, categorized by type (book, magazine, digital media).
Borrowing: Logs borrowing activities, including late fee calculations.
Author: Stores author information.
Publisher: Tracks publisher details.
FeePolicy: Defines role-based late fee structures.
ResourceType: Details classifications for resources.
Key Technical Highlights
Primary and Foreign Keys

Primary Keys uniquely identify records in all relations (e.g., userID, resourceID, borrowID).
Foreign Keys enforce relationships between tables (e.g., User.userID → Borrowing.userID).
Referential Integrity

Implemented through foreign key constraints to ensure consistent and valid references across tables.

Normalization

The schema is normalized to reduce redundancy and achieve Third Normal Form (3NF). Dependencies between attributes are minimized for better data consistency and maintainability.

Setup Instructions
Database Setup:
Use the SQL scripts in LMS_Scripts.sql to create the schema and populate initial data.
Dependencies:
Relational database management system (MySQL).
Execution:
Import the schema into your database and test the system using the provided sample queries.
Future Enhancements
Enhanced Reporting: Add support for generating detailed reports on borrowing trends, resource availability, and user activity.
Recommendation System: Introduce personalized recommendations based on borrowing history.
Mobile App Integration: Enable seamless access to the system via mobile applications.

