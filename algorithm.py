def get_queen_valid(n, queens, new_queen):
    if new_queen in queens:
        return False

    for row, queen in enumerate(queens):
        if abs(new_queen - queen) == abs(len(queens) - row):
            return False

    return True

def solve(n):
    stack = [[i] for i in reversed(range(n))]
    while len(stack) > 0:
        queens = stack.pop()

        if len(queens) == n:
            return queens

        for new_queen in range(n):
            if get_queen_valid(n, queens, new_queen):
                yield queens + [new_queen]
                stack.append(queens + [new_queen])