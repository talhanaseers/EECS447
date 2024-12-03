SELECT r.title, COUNT(b.borrowID) AS timesBorrowed
FROM Borrowing b
JOIN Resource r ON b.resourceID = r.resourceID
GROUP BY r.title
ORDER BY timesBorrowed DESC;
