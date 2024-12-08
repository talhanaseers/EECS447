SELECT 
    r.resourceID,
    r.title,
    r.availableCopies,
    r.totalCopies
FROM 
    Resource r
WHERE 
    r.type = 'Book' 
    AND r.availableCopies > 0;

