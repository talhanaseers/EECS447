ALTER TABLE FeePolicy
    ADD CONSTRAINT chk_baseFee CHECK (baseFee >= 0),
    ADD CONSTRAINT chk_maxFee CHECK (maxFee >= baseFee);

ALTER TABLE User
    ADD CONSTRAINT chk_status CHECK (status IN ('Active', 'Expired', 'Suspended'));

ALTER TABLE Resource
    ADD CONSTRAINT chk_available_copies CHECK (availableCopies <= totalCopies);

ALTER TABLE Borrowing
    ADD CONSTRAINT chk_due_date CHECK (dueDate >= borrowDate),
    ADD CONSTRAINT fk_userID FOREIGN KEY (userID) REFERENCES User(userID),
    ADD CONSTRAINT fk_resourceID FOREIGN KEY (resourceID) REFERENCES Resource(resourceID),
    ADD CONSTRAINT fk_policyID FOREIGN KEY (policyID) REFERENCES FeePolicy(policyID);
