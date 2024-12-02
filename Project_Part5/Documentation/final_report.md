# **Final Report: Library Management System Database**

---

## **Course Information**  
**Course**: EECS 447 – Database Systems  
**Instructor**: Professor Dr. Hossein Saidian  
**Submission Date**: December 3, 2024  

---

## **Team Information**  
**Team Name**: The Databasers 

**Team Members**:  
- Talha Naseer  
- 
-   

---

## **Project Overview**

The **Library Management System (LMS)** is a comprehensive database designed to optimize the operational efficiency of libraries by managing resources, memberships, and borrowing activities. The database adheres to relational database principles and is implemented in MySQL, ensuring scalability, data integrity, and ease of use.

---

### **Objectives**
1. **Efficient Resource Management**: Track library materials, including books, magazines, and digital resources.  
2. **Membership Oversight**: Maintain user profiles, borrowing history, and membership statuses.  
3. **Operational Insights**: Generate analytics reports for key metrics, such as borrowing trends.  
4. **Data Integrity**: Enforce robust constraints for referential integrity and minimize redundancy.  
5. **Future Scalability**: Create a database that can evolve with additional features like mobile integration.

---

## **Database Schema**

### **Relational Schema**
The LMS database contains the following core relations:  
1. **Users**: Tracks user details and roles (e.g., Admin, Member).  
2. **Resources**: Manages inventory of books, magazines, and digital resources.  
3. **Borrowing**: Logs borrowing activities, due dates, and late fees.  
4. **Authors**: Maintains author information.  
5. **Publishers**: Tracks publisher details.  
6. **FeePolicy**: Implements role-based fee structures.  
7. **ResourceType**: Categorizes resources (e.g., books, magazines, media).  

The schema adheres to **Third Normal Form (3NF)** to ensure minimal redundancy and optimal performance.

### **Diagram**
Refer to the **Relational_Schema_Diagram.png** in the repository for a visual representation of the schema.  

---

## **Key Features**

### **Normalization**
The schema has been normalized to 3NF:
- Attributes are functionally dependent only on the primary key.
- Redundancy is minimized, improving data integrity and maintainability.

### **Constraints**
- **Primary Keys**: Ensure unique record identification.
- **Foreign Keys**: Maintain relationships between tables and enforce referential integrity.
- **Domain Constraints**: Restrict values to specific ranges or types (e.g., dates for borrowing transactions).

### **Role-Based Policies**
The system implements differentiated borrowing limits and late fee policies for Admins and Members.

---

## **Setup Instructions**

1. **Prerequisites**:  
   - MySQL 8.0+ installed on your system.  
   - SQL client software such as MySQL Workbench or a compatible alternative.  

2. **Database Initialization**:  
   Run the provided `LMS_Scripts.sql` file to create the schema and populate it with initial data.

3. **Testing the Setup**:  
   Use the included sample queries in `Sample_Queries.sql` to validate database functionality.

---

## **Progress Tracker**

| **Date**       | **Tasks Completed**                                                                 | **Decisions/Changes**                                                                                   |
|-----------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Nov 28, 2024**| Finalized the database schema and began ER diagram creation.                        | No changes made to initial plan.                                                                       |
| **Nov 29, 2024**| Converted the ER diagram into relational schema and started writing SQL scripts.    | Adjusted cardinalities for `Borrowing` relation to accommodate multiple borrow-return cycles.           |
| **Nov 30, 2024**| Tested SQL scripts for schema creation and data insertion.                         | Added additional constraints for late fee calculations.                                                |
| **Dec 1, 2024** | Created documentation for schema and setup instructions.                           | Clarified relationships in `ResourceType` table for better granularity.                                |
| **Dec 2, 2024** | Finalized and reviewed documentation, relational schema, and test queries.          | No major changes.                                                                                      |
| **Dec 3, 2024** | Submitted the final project report and ensured repository readiness for submission. | No changes.                                                                                            |

---

## **Future Enhancements**

1. **Mobile App Integration**: Expand the database to integrate seamlessly with mobile applications for user convenience.
2. **Recommendation Engine**: Implement a module to suggest resources based on user borrowing history.
3. **Enhanced Analytics**: Introduce detailed reporting capabilities for library administrators.

---

## **Contributors**
- **Talha Naseer**: Team Administrator, Documentation, SQL Scripts  
- **[]**: ER Diagram, Testing  
- **[]**: Schema Design, Normalization
- etc etc

---

## **Folder Structure**
```plaintext
├── Relational_Schema_Diagram.png    # Visual representation of the schema
├── LMS_Scripts.sql                  # SQL scripts for schema creation and data population
├── Sample_Queries.sql               # Test queries for database validation
├── DataDictionary.md                # Detailed data dictionary
├── Final_Report.md                  # Final project report
└── README.md                        # Project overview and setup instructions
