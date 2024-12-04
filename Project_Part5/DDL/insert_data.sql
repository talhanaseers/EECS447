INSERT INTO User (userID, name, role, email, phone, status, membershipValidUntil) VALUES
    (1, 'Alice Johnson', 'Admin', 'alice@example.com', '123-456-7890', 'Active', '2025-12-31'),
    (2, 'Bob Smith', 'Member', 'bob@example.com', '987-654-3210', 'Active', '2024-06-30'),
    (3, 'Charlie Davis', 'Member', 'charlie@example.com', NULL, 'Expired', '2023-12-31');

INSERT INTO Author (authorID, name, biography) VALUES
    (1, 'J.K. Rowling', 'Author of the Harry Potter series.'),
    (2, 'George R.R. Martin', 'Author of the A Song of Ice and Fire series.'),
    (3, 'Isaac Asimov', 'Prolific science fiction writer.');

INSERT INTO Publisher (publisherID, name, address) VALUES
    (1, 'Bloomsbury Publishing', '50 Bedford Square, London'),
    (2, 'Bantam Books', '1745 Broadway, New York, NY'),
    (3, 'Doubleday', '1745 Broadway, New York, NY');

INSERT INTO FeePolicy (policyID, baseFee, maxFee) VALUES
    (1, 0.50, 20.00),
    (2, 1.00, 25.00),
    (3, 0.75, 15.00);

INSERT INTO Resource (resourceID, title, type, authorID, publisherID, availableCopies, totalCopies) VALUES
    (1, 'Harry Potter and the Philosopher''s Stone', 'Book', 1, 1, 5, 10),
    (2, 'A Game of Thrones', 'Book', 2, 2, 2, 5),
    (3, 'Foundation', 'Book', 3, 3, 4, 4),
    (4, 'Scientific American - June 2024', 'Magazine', NULL, 3, 10, 10),
    (5, 'Inception', 'Digital Media', NULL, NULL, 3, 3);

INSERT INTO Borrowing (borrowID, userID, resourceID, borrowDate, returnDate, dueDate, lateFee, policyID) VALUES
    (1, 2, 1, '2024-01-15', '2024-01-22', '2024-01-20', NULL, 1),
    (2, 3, 2, '2023-12-01', '2023-12-10', '2023-12-07', 1.50, 2),
    (3, 2, 3, '2024-03-01', NULL, '2024-03-15', NULL, 1);
