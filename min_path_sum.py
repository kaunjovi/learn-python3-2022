class MinimumPathSum: 
    def minPathSum(self, grid: list[list[int]]) -> int:
        row_count = len(grid)
        col_count = len(grid[0])
        print(f"Row count = {row_count}. Column count = {col_count}")

        return 10 

calculation = MinimumPathSum()
grid = [[1,3,1],[1,5,1],[4,2,1]]
min_sum = calculation.minPathSum(grid)
print(f"The minimum path sum is {min_sum}")


