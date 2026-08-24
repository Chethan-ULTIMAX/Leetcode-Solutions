-- File: 1757_recyclable_and_low_fat_products.sql

-- Problem: Recyclable and Low Fat Products
-- LeetCode: 1757
--
-- Approach: Filtering
-- -------------------
-- Select products that satisfy both conditions:
-- 1. low_fats is 'Y'
-- 2. recyclable is 'Y'
--
-- Time Complexity: O(n)
-- Space Complexity: O(1)

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';
