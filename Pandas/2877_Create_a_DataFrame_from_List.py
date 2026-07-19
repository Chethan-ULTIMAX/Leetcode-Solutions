# Problem: Create a DataFrame from List
# LeetCode: 2877
#
# Approach: Pandas DataFrame
# --------------------------
# Create a DataFrame from the given list of student
# information and assign appropriate column names.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

import pandas as pd

def createDataframe(student_data):
    """
    :type student_data: List[List[int]]
    :rtype: pd.DataFrame
    """

    return pd.DataFrame(
        student_data,
        columns=["student_id", "age"]
    )
