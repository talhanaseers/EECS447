--This wont work as Resource ID is a foreign key in the borrowing table

--DELETE FROM Resource
--WHERE resourceID = 1001;

--Here is a more accurate functionality to delete a resource
-- Delete dependent rows from the Borrowing table first
DELETE FROM Borrowing
WHERE resourceID = 1001;

-- Now delete the resource from the Resource table
DELETE FROM Resource
WHERE resourceID = 1001;
