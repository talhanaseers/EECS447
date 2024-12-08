SELECT 
    a.authorID,
    a.name AS authorName,
    COUNT(b.borrowID) AS borrowCount
FROM 
    Borrowing b
JOIN 
    Resource r ON b.resourceID = r.resourceID
JOIN 
    Author a ON r.authorID = a.authorID
WHERE 
    b.borrowDate >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
GROUP BY 
    a.authorID, a.name
ORDER BY 
    borrowCount DESC
LIMIT 1;

