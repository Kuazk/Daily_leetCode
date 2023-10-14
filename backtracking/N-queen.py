class QueensProblem:

    def __init__(self,n):
        self.n = n 
        self.chess_table = [[0 for i in range(n)] for j in range(n)]
    
    def solve_n_queens(self):

        if self.solve(0):
            self.print_queens()
        else:
            print("no solution")
    def solve(self, col_index):
        if col_index == self.n:
            return True
        
        for row_index in range(self.n):
            if self.is_place_vallid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1
                
                if self.solve(col_index+1):
                    return True 
                
                # backTrack
                self.chess_table[row_index][col_index] = 0
        return False

    def print_queens(self):
        for row in self.chess_table:
            print(row)


queens = QueensProblem(4)
queens.print_queens()