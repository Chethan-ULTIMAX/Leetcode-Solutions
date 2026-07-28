-- Problem: Sales Person
-- LeetCode: 607
--
-- Approach: Subquery with NOT IN
-- ------------------------------
-- Find the salespersons who have never made
-- a sale to the company named 'RED'.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT
    name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    WHERE com_id = (
        SELECT com_id
        FROM Company
        WHERE name = 'RED'
    )
);
