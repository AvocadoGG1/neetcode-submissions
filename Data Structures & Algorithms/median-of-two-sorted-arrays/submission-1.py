class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Give nums1 and nums2 shorter names
        A, B = nums1, nums2

        # Total number of elements across BOTH arrays
        # Example: [1, 3] and [2, 4] -> total = 4
        total = len(nums1) + len(nums2)

        # How many elements we want on the LEFT half
        # Example: total = 4 -> half = 2
        half = total // 2

        # We want A to ALWAYS be the smaller array
        # This is important because we will binary search A
        if len(B) < len(A):
            A, B = B, A  # swap A and B

        # Binary search boundaries for A
        l = 0
        r = len(A) - 1

        # Keep searching until we find the correct partition
        while True:

            # i is the last index on the LEFT side of A
            i = (l + r) // 2

            # j is the last index on the LEFT side of B
            # We calculate j so the total LEFT side has `half` elements
            j = half - i - 2

            # Get the biggest value on the LEFT side of A
            # If A has nothing on its left side, pretend it's -infinity
            Aleft = A[i] if i >= 0 else float("-infinity")

            # Get the smallest value on the RIGHT side of A
            # If A has nothing on its right side, pretend it's +infinity
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            # Get the biggest value on the LEFT side of B
            # If B has nothing on its left side, pretend it's -infinity
            Bleft = B[j] if j >= 0 else float("-infinity")

            # Get the smallest value on the RIGHT side of B
            # If B has nothing on its right side, pretend it's +infinity
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Check whether we found the correct partition
            #
            # Everything on the LEFT must be <= everything on the RIGHT
            if Aleft <= Bright and Bleft <= Aright:

                # If total is ODD, there is one middle value
                # The median is the smallest value on the RIGHT
                if total % 2:
                    return min(Aright, Bright)

                # If total is EVEN, there are two middle values
                # biggest value on LEFT + smallest value on RIGHT
                # then divide by 2
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Aleft is too big
            # We took too many elements from A
            # Move A's partition to the LEFT
            elif Aleft > Bright:
                r = i - 1

            # Otherwise Bleft > Aright
            # We didn't take enough elements from A
            # Move A's partition to the RIGHT
            else:
                l = i + 1

