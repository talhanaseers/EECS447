SELECT 
    AVG(DATEDIFF(
        COALESCE(b.returnDate, CURDATE()), -- Use the return date or the current date for ongoing borrowings
        b.borrowDate
    )) AS avgBorrowingDays
FROM 
    Borrowing b
JOIN 
    Resource r ON b.resourceID = r.resourceID
WHERE 
    r.type = 'Book';

