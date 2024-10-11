# Library Management System - Database Requirements Document

## Tasks

### 1. Introduction

**Project Overview:**  
The Library Management System is designed to manage a library’s inventory of books, digital media, and magazines, along with client memberships and borrowing activities. The database will facilitate efficient tracking of item availability, enforcing borrowing limits, calculating late fees, and generating reports.

**Scope:**  
The project involves the development of a relational database that supports multi-user environments and includes transaction management and role-based access control. It will not cover non-library related resources or financial services beyond library fees.

**Glossary:**
- **Library Resource:** Any item (book, digital media, magazine) available for borrowing.
- **Borrowing Rules:** Constraints on how many items a user can borrow and for how long.
- **Late Fees:** Fines applied to overdue borrowed items.
- **User Role:** The specific access level assigned to a user (e.g., Admin, Member).
- **Transaction Management:** Ensuring that all database changes are applied reliably in multi-user scenarios.

---

### 2. Stakeholders

- **Library Administrators:**  
  Manage library resources, memberships, borrowing rules, and generate reports.
  
- **Library Members:**  
  End-users who will borrow and return library resources, manage their accounts, and pay fines.

- **System Administrators:**  
  Maintain the database, ensure smooth operations, and implement security measures.

---

### 3. Requirements

**Functional Requirements:**
- **User Management:**  
  Administrators can add, update, or delete user accounts and manage user roles.

- **Resource Management:**  
  The system will support the addition, removal, and update of books, magazines, and digital media.

- **Borrowing Management:**  
  Users can check out and return resources, and administrators can enforce borrowing limits and apply late fees.

- **Search and Reporting:**  
  The system will support querying for resource availability, borrowing history, and generate reports on resource usage, user activity, and overdue items.

**Non-Functional Requirements (Optional):**
- **Performance:**  
  The database should support concurrent users and maintain a response time of less than 2 seconds for typical queries.
  
- **Security:**  
  The system must enforce user authentication, encryption of sensitive data, and role-based access to resources.

---

### 4. Data Requirements

**Data Entities:**
1. **User:**
   - Attributes: userID (int), name (varchar), role (enum: 'Admin', 'Member'), email (varchar), phone (varchar).
   
2. **Resource:**
   - Attributes: resourceID (int), title (varchar), type (enum: 'Book', 'Magazine', 'Digital Media'), author (varchar), availableCopies (int), totalCopies (int).
   
3. **Borrowing:**
   - Attributes: borrowID (int), userID (int), resourceID (int), borrowDate (date), returnDate (date), dueDate (date), lateFee (decimal).

---

### 5. User Requirements

**User Types:**
1. **Admin Users:**  
   Can manage library resources, user accounts, borrowing rules, and generate reports.
   
2. **Member Users:**  
   Can borrow, return, and search for resources, as well as view their borrowing history and any associated late fees.

**Interface Requirements:**
- A user-friendly interface with simple search, borrowing, and return functionalities for members.
- Administrative functions for managing the database, resources, and users should be accessible through secure login.

---

### 6. Hardware and Software Requirements

- **Hardware:**
  - A server with sufficient resources to support the database (4 GB RAM, 100 GB storage).
  
- **Software:**
  - **Database Management System:** MySQL or MariaDB.
  - **Operating System:** Linux (EECS servers) or Windows/MacOS (for development).
  - **Development Tools:** Visual Studio Code, GitHub for version control.

---

### 7. Appendices

Include any additional information such as diagrams, flowcharts, or example queries if necessary in future versions.

---

### 8. GitHub Repository Management

The team will continue to manage the repository, following the same guidelines from the project vision. GitFlow will be used to organize branches for development and features, and GitHub Actions will automate testing and code quality checks.
