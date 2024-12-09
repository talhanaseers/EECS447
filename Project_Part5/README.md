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
│
├── Additional Queries (Assigned December 5)/       # Additional SQL Queries (Alternative to live team demos — Assigned December 5, 2024)
│   ├── Fine_Calculation.sql                        # Additional SQL Query
│   ├── FineCalculation.png                         # Additional SQL Query Screenshot
│   ├── Book_Availability.sql                       # Additional SQL Query
│   ├── BookAvailability.png                        # Additional SQL Query Screenshot
│   ├── Frequent_Borrowers_of_a_Specific_Genre.sql  # Additional SQL Query
│   ├── FrequentBorrowersOfSameGenre.png            # Additional SQL Query Screenshot
│   ├── Books_Due_Soon.sql                          # Additional SQL Query
│   ├── BooksDueSoon.png                            # Additional SQL Query Screenshot
│   ├── Members_with_Overdue_Books.sql              # Additional SQL Query
│   ├── MembersWithOverdueBooks.png                 # Additional SQL Query Screenshot
│   ├── Average_Borrowing_Time.sql                  # Additional SQL Query
│   ├── AverageBorrowingTime.png                    # Additional SQL Query Screenshot
│   ├── MostPopularAuthorInTheLastMonth.png         # Additional SQL Query Screenshot
│   └── Most_Popular_Author_in_the_Last_Month.sql   # Additional SQL Query
│
├── SQL Report (Assigned December 5)/               # SQL Report and Output Screenshot (Alternative to live team demos — Assigned December 5, 2024)
│   ├── Operational_Efficiency_Report.md            # Operational Efficiency Report Assigned
│   ├── average_borrowing_time.png                  # Screenshot of query output from SQL Report
│   ├── bottleneck_analysis.png                     # Screenshot of query output from SQL Report
│   ├── fine_collection_trends.png                  # Screenshot of query output from SQL Report
│   ├── overdue_book_rates.png                      # Screenshot of query output from SQL Report
│   └── peak_borrowing_periods.png                  # Screenshot of query output from SQL Report
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
