SELECT 
    u.userID,
    u.name,
    u.email,
    SUM(
        CASE
            WHEN b.returnDate IS NULL AND CURDATE() > b.dueDate THEN
                DATEDIFF(CURDATE(), b.dueDate) * 0.25
            WHEN b.returnDate > b.dueDate THEN
                DATEDIFF(b.returnDate, b.dueDate) * 0.25
            ELSE
                0
        END
    ) AS totalFine
FROM 
    Borrowing b
JOIN 
    User u ON b.userID = u.userID
WHERE 
    u.status = 'Active' -- Only consider active members
GROUP BY 
    u.userID, u.name, u.email
HAVING 
    totalFine > 0; -- Only show members who owe fines

