SELECT resourceID, title, type, availableCopies, totalCopies
FROM Resource
WHERE availableCopies > 0;
