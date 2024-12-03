UPDATE Borrowing
SET returnDate = '2024-12-02'
WHERE borrowID = 1;

UPDATE Resource
SET availableCopies = availableCopies + 1
WHERE resourceID = 1001;
