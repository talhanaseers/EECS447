SELECT b.borrowID, u.name AS userName, r.title, b.dueDate, DATEDIFF(CURRENT_DATE, b.dueDate) AS daysOverdue
FROM Borrowing b
JOIN User u ON b.userID = u.userID
JOIN Resource r ON b.resourceID = r.resourceID
WHERE b.returnDate IS NULL AND b.dueDate < CURRENT_DATE
  LIMIT 10; --Only prints the first 10 results for testing
