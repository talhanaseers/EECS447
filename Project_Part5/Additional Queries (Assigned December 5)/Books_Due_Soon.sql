SELECT 
    b.borrowID,
    r.resourceID,
    r.title,
    u.userID,
    u.name AS borrowerName,
    b.dueDate
FROM 
    Borrowing b
JOIN 
    Resource r ON b.resourceID = r.resourceID
JOIN 
    User u ON b.userID = u.userID
WHERE 
    r.type = 'Book'
    AND b.dueDate BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
ORDER BY 
    b.dueDate ASC;

