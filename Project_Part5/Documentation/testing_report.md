-- DATABASE TEST CASES SCRIPT WITH EXPLANATIONS

-- 1. Apply Late Fees
-- Test to calculate and apply late fees for overdue borrowings.
-- The query calculates the late fee using the difference between the return date and due date,
-- multiplied by a base fee, and updates only overdue borrowings.
UPDATE Borrowing
SET lateFee = GREATEST(0, (DATEDIFF(returnDate, dueDate) * 
              (SELECT baseFee FROM FeePolicy WHERE policyID = Borrowing.policyID)))
WHERE returnDate > dueDate;

-- 2. Checkout Resource
-- Test to insert a new borrowing record.
-- The query simulates a user checking out a resource by recording borrowing details.
INSERT INTO Borrowing (borrowID, userID, resourceID, borrowDate, dueDate, lateFee, policyID)
VALUES (6001, 1, 1001, '2024-11-24', '2024-12-01', 0.00, 1);

-- 3. Return Resource
-- Test to update the return date of a borrowing and increment the available copies of the resource.
-- The query simulates a user returning a resource.
UPDATE Borrowing
SET returnDate = '2024-12-02'
WHERE borrowID = 1;

UPDATE Resource
SET availableCopies = availableCopies + 1
WHERE resourceID = 1001;

-- 4. Add New Resource
-- Test to insert a new resource into the database.
-- The first attempt will fail due to a duplicate primary key, while the second succeeds with a unique resource ID.
INSERT INTO Resource (resourceID, title, type, authorID, publisherID, availableCopies, totalCopies)
VALUES (1001, 'Digital Signal Processing', 'Book', 1, 1, 5, 5);

INSERT INTO Resource (resourceID, title, type, authorID, publisherID, availableCopies, totalCopies)
VALUES (12373484, 'Digital Signal Processing', 'Book', 1, 1, 5, 5);

-- 5. Remove Resource
-- Test to delete a resource from the database.
-- This query fails because of a foreign key constraint, ensuring the database maintains referential integrity.
DELETE FROM Resource
WHERE resourceID = 1001;

-- 6. Update Available Copies
-- Test to decrement the available copies of a resource when it is borrowed.
-- The query ensures that only resources with `availableCopies > 0` are updated.
UPDATE Resource
SET availableCopies = availableCopies - 1
WHERE resourceID = 1001 AND availableCopies > 0;

-- 7. Overdue Item Report
-- Test to generate a report of overdue borrowings.
-- The query joins Borrowing, User, and Resource tables to list overdue items,
-- including user names, titles, due dates, and days overdue.
SELECT b.borrowID, u.name AS userName, r.title, b.dueDate, 
       DATEDIFF(CURRENT_DATE, b.dueDate) AS daysOverdue
FROM Borrowing b
JOIN User u ON b.userID = u.userID
JOIN Resource r ON b.resourceID = r.resourceID
WHERE b.returnDate IS NULL AND b.dueDate < CURRENT_DATE
LIMIT 10;

-- 8. Resource Availability Report
-- Test to display resources with available copies.
-- The query ensures that only resources with `availableCopies > 0` are included in the report.
SELECT resourceID, title, type, availableCopies, totalCopies
FROM Resource
WHERE availableCopies > 0
LIMIT 10;

-- 9. Resource Usage Report
-- Test to display how much each resource has been used (borrowed).
-- This query aggregates borrowing counts for all resources.
SELECT r.title, COUNT(b.borrowID) AS timesBorrowed
FROM Borrowing b
JOIN Resource r ON b.resourceID = r.resourceID
GROUP BY r.title
ORDER BY timesBorrowed DESC;

-- 10. Top Ten Borrowed Resources Report
-- Test to display the top ten most borrowed resources.
-- This query is the same as the Resource Usage Report but limits the results to the top 10.
SELECT r.title, COUNT(b.borrowID) AS timesBorrowed
FROM Borrowing b
JOIN Resource r ON b.resourceID = r.resourceID
GROUP BY r.title
ORDER BY timesBorrowed DESC
LIMIT 10;

-- 11. Add User
-- Test to add a new user to the database.
-- The query ensures the database can successfully add new users without primary key conflicts.
INSERT INTO User (userID, name, role, email, phone, status, membershipValidUntil)
VALUES (89756, 'John Doe', 'Member', 'john.doe@example.com', '123-456-7890', 'Active', '2025-12-31');

-- 12. Delete User
-- Test to delete a user from the database.
-- This query fails because of a foreign key constraint, ensuring no orphaned references exist in dependent tables.
DELETE FROM User
WHERE userID = 1;

-- 13. Set User Role
-- Test to update a user's role in the database.
-- The query ensures the user's role can be updated without issues.
UPDATE User
SET role = 'Admin'
WHERE userID = 1;

-- 14. User Borrowing History
-- Test to display the borrowing history for a specific user.
-- This query joins Borrowing and Resource tables to list all borrowings for a given user ID.
SELECT b.borrowID, r.title, b.borrowDate, b.dueDate, b.returnDate, b.lateFee
FROM Borrowing b
JOIN Resource r ON b.resourceID = r.resourceID
WHERE b.userID = 1;

