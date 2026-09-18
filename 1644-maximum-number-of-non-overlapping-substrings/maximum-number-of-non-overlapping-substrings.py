class Solution:
    def maxNumOfSubstrings(self, s):
        first = {}
        last = {}

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Create the smallest valid interval for each character
        for ch in first:
            left = first[ch]
            right = last[ch]
            i = left
            valid = True

            while i <= right:
                c = s[i]

                # This character appeared before our interval
                if first[c] < left:
                    valid = False
                    break

                # Expand the interval
                right = max(right, last[c])
                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        # Select non-overlapping intervals
        for left, right in intervals:
            if left > end:
                result.append(s[left:right + 1])
                end = right

        return result