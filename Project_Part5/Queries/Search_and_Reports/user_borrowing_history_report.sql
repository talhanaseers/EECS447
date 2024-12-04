SELECT b.borrowID, r.title, b.borrowDate, b.dueDate, b.returnDate, b.lateFee
FROM Borrowing b
JOIN Resource r ON b.resourceID = r.resourceID
WHERE b.userID = 1;
