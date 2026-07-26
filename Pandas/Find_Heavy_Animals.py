# Problem: Find Heavy Animals
#
# Approach: Filtering and Sorting
# -------------------------------
# Filter animals with weight greater than 100,
# sort them in descending order by weight,
# and return only the 'name' column.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """
    :type animals: pd.DataFrame
    :rtype: pd.DataFrame
    """

    return (
        animals[animals["weight"] > 100]
        .sort_values(by="weight", ascending=False)
        [["name"]]
    )
