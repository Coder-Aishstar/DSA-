class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Segment tree
        size = 1
        while size < n:
            size *= 2

        # tree[node] = [product % k, count of prefix products]
        tree = [(1 % k, [0] * k) for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            val = nums[i] % k
            cnt = [0] * k
            cnt[val] = 1
            tree[size + i] = (val, cnt)

        # Merge two nodes
        def merge(left, right):
            lp, lc = left
            rp, rc = right

            count = lc[:]

            for r in range(k):
                count[(lp * r) % k] += rc[r]

            return ((lp * rp) % k, count)

        # Build tree
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        # Update one index
        def update(pos, value):
            pos += size
            value %= k

            cnt = [0] * k
            cnt[value] = 1
            tree[pos] = (value, cnt)

            pos //= 2

            while pos:
                tree[pos] = merge(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        # Query [left, right]
        def query(left, right):
            left += size
            right += size

            left_nodes = []
            right_nodes = []

            while left <= right:
                if left % 2 == 1:
                    left_nodes.append(tree[left])
                    left += 1

                if right % 2 == 0:
                    right_nodes.append(tree[right])
                    right -= 1

                left //= 2
                right //= 2

            result = (1 % k, [0] * k)

            for node in left_nodes:
                result = merge(result, node)

            for node in reversed(right_nodes):
                result = merge(result, node)

            return result

        answer = []

        for index, value, start, x in queries:
            # Permanent update
            update(index, value)

            # Query suffix [start, n-1]
            _, count = query(start, n - 1)

            answer.append(count[x])

        return answer
        