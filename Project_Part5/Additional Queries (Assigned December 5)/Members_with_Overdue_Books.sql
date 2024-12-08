SELECT 
    u.userID,
    u.name AS borrowerName,
    u.email,
    r.title AS overdueBookTitle,
    b.dueDate
FROM 
    Borrowing b
JOIN 
    User u ON b.userID = u.userID
JOIN 
    Resource r ON b.resourceID = r.resourceID
WHERE 
    r.type = 'Book' 
    AND b.returnDate IS NULL -- Book has not been returned
    AND b.dueDate < CURDATE() -- Due date has passed
ORDER BY 
    u.userID, b.dueDate ASC;

