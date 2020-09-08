from typing import List


# we'll present a single (particular) solution by a list of col positions with indices representing rows
# e.g. [1, 3, 0, 2] - queen at row 0 is at column, queen at row 1 is at column 3, etc.


def n_queens(n: int) -> List[List[int]]:  # find all the ways we can put the n queens
    result: List[List[int]] = []
    solve_n_queens(n=n, row=0, col_placement=[], result=result)

    return result


def solve_n_queens(
        n: int,
        row: int,
        col_placement: List[int],
        result: List[List[int]]
):
    if row == n:
        result.append(col_placement.copy())
    else:
        # for each possible column in current row (curr row is the next in col_placement indices)
        # try to find solutions
        for col in range(n):
            col_placement.append(col)
            if is_valid(col_placement):
                solve_n_queens(n, row + 1, col_placement, result)
            col_placement.pop()


def is_valid(col_placements: List[int]) -> bool:
    curr_row = len(col_placements) - 1
    curr_col = col_placements[curr_row]

    for prev_row in range(len(col_placements) - 1):  # all previous rows
        prev_col = col_placements[prev_row]

        if (curr_col == prev_col  # same column means columns are equal
                or curr_row - prev_row == abs(curr_col - prev_col)):  # travel on x and travel on y is equal
            return False

    return True


print(n_queens(4))

assert is_valid([0,0]) is False