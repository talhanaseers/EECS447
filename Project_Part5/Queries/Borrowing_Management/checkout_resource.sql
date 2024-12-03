INSERT INTO Borrowing (borrowID, userID, resourceID, borrowDate, dueDate, lateFee, policyID)
VALUES (1, 1, 1001, '2024-11-24', '2024-12-01', 0.00, 1);

UPDATE Resource
SET availableCopies = availableCopies - 1
WHERE resourceID = 1001 AND availableCopies > 0;
