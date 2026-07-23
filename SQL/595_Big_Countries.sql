-- Problem: Big Countries
-- LeetCode: 595
--
-- Approach: WHERE Clause
-- ----------------------
-- Select the country name, population, and area.
-- A country is considered "big" if:
--   - Population is at least 25,000,000, or
--   - Area is at least 3,000,000 square kilometers.
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT
    name,
    population,
    area
FROM World
WHERE population >= 25000000
   OR area >= 3000000;
