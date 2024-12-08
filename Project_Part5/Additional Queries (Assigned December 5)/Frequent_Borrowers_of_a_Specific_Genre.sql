SELECT 
    u.userID,
    u.name,
    u.email,
    COUNT(b.borrowID) AS booksBorrowed
FROM 
    Borrowing b
JOIN 
    User u ON b.userID = u.userID
JOIN 
    Resource r ON b.resourceID = r.resourceID
WHERE 
    r.type = 'Book'
    AND b.borrowDate >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY 
    u.userID, u.name, u.email
ORDER BY 
    booksBorrowed DESC
LIMIT 10; -- Adjust the limit as needed

