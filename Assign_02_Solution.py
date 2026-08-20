from collections import deque


def quickestWayUp(ladders, snakes):
    jumps = {}

    # Store ladders
    for start, end in ladders:
        jumps[start] = end

    # Store snakes
    for start, end in snakes:
        jumps[start] = end

    # Distance array
    distance = [-1] * 101
    distance[1] = 0

    # BFS
    queue = deque()
    queue.append(1)

    while queue:
        current = queue.popleft()

        # Try dice values 1 to 6
        for dice in range(1, 7):
            next_square = current + dice

            if next_square > 100:
                continue

            # Take ladder or snake
            if next_square in jumps:
                next_square = jumps[next_square]

            # Visit if not already visited
            if distance[next_square] == -1:
                distance[next_square] = distance[current] + 1
                queue.append(next_square)

    return distance[100]


if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            a, b = map(int, input().split())
            ladders.append([a, b])

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            a, b = map(int, input().split())
            snakes.append([a, b])

        result = quickestWayUp(ladders, snakes)

        print(result)