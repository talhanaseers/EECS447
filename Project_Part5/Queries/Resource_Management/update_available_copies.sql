UPDATE Resource
SET availableCopies = availableCopies - 1
WHERE resourceID = 1001 AND availableCopies > 0;
