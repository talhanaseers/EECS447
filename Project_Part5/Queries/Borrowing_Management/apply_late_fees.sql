UPDATE Borrowing
SET lateFee = GREATEST(0, (DATEDIFF(returnDate, dueDate) * (SELECT baseFee FROM FeePolicy WHERE policyID = Borrowing.policyID)))
WHERE returnDate > dueDate
AND EXISTS (
    SELECT 1
    FROM User
    WHERE userID = <adminUserID> AND role = 'Admin'
);
