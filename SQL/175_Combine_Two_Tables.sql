-- Problem: Combine Two Tables
-- LeetCode: 175
--
-- Approach: LEFT JOIN
-- -------------------
-- Retrieve each person's first name and last name.
-- Use a LEFT JOIN to include all records from the
-- Person table, even if no matching address exists.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId;
