# def solution(n, m, figure):
#     """
#     Arrange custom block pieces on an N×M grid.
    
#     Args:
#         n (int): Height of the grid
#         m (int): Width of the grid  
#         figure (list): List of block types ['A', 'B', 'C', 'D', 'E']
    
#     Returns:
#         list: 2D grid arrangement
#     """
    
#     # Initialize empty grid
#     gd = [[0 for _ in range(m)] for _ in range(n)]
    
    
#     A = [(0, 0)]                                    # Single block
#     B = [(0, 0), (0, 1), (0, 2)]               # 3 horizontal
#     C = [(0, 0), (0, 1), (1, 0), (1, 1)]     # 2x2 box
#     D = [(0, 0), (1, 0), (2, 0), (1, 1)]     # T-shape (3 vertical + 1 middle horizontal)
#     E = [(0, 0), (0, 1), (0, 2), (1, 1)]
#     # Define block shapes (relative coordinates)
#     blocks = {
#         'A': A,                                    # Single block
#         'B': B,                # 3 horizontal
#         'C': C,        # 2x2 box
#         'D': D,          # T-shape (3 vertical + 1 middle horizontal)
#         'E': E       # Upside-down T (3 horizontal + 1 middle up)
#     }
    
#     # Try to place each piece
#     for pnum, btype in enumerate(figure, 1):
#         if btype not in blocks:
#             continue
            
#         block = blocks[btype]
#         pl = False
        
#         # Try all positions until piece fits
#         for startn in range(n):
#             for startc in range(m):
#                 # Check if piece fits at this position
#                 cpl = True
#                 for r, c in block:
#                     ra, ca = startn + r, startc + c
#                     if r >= n or c >= m or gd[ra][ca] != 0:
#                         cpl = False
#                         break
                
#                 # Place the piece if it fits
#                 if cpl:
#                     for dr, dc in block:
#                         r, c = startn + r, startc + c
#                         gd[ra][ca] = pnum
#                     pl = True
#                     break
            
#             if pl:
#                 break
    
#     return gd


# if __name__ == "__main__":
#     n =  4
#     m = 4
#     f = ['D','b','A','C']
#     show = solution(n,m,f)
#     print(show)


def solution(n, m, figure):
    """
    Arrange custom block pieces on an N×M grid with smart placement.
    
    Args:
        n (int): Height of the grid
        m (int): Width of the grid  
        figure (list): List of block types ['A', 'B', 'C', 'D', 'E']
    
    Returns:
        list: 2D grid arrangement
    """
    
    # Initialize empty grid
    grid = [[0 for _ in range(m)] for _ in range(n)]
    
    # Define block shapes (relative coordinates)
    shapes = {
        'A': [(0, 0)],                                    # Single block
        'B': [(0, 0), (0, 1), (0, 2)],                  # 3 horizontal
        'C': [(0, 0), (0, 1), (1, 0), (1, 1)],          # 2x2 box
        'D': [(0, 0), (1, 0), (2, 0), (1, 1)],          # T-shape (3 vertical + 1 middle horizontal)
        'E': [(0, 0), (0, 1), (0, 2), (1, 1)]           # Upside-down T (3 horizontal + 1 middle up)
    }
    
    def can_place_piece(grid, shape, start_row, start_col):
        """Check if piece can be placed at given position"""
        for dr, dc in shape:
            r, c = start_row + dr, start_col + dc
            if r >= n or c >= m or r < 0 or c < 0 or grid[r][c] != 0:
                return False
        return True
    
    def place_piece(grid, shape, start_row, start_col, piece_num):
        """Place piece on grid"""
        for dr, dc in shape:
            r, c = start_row + dr, start_col + dc
            grid[r][c] = piece_num
    
    def get_best_position(grid, shape):
        """Find the best position to place a piece (compact arrangement)"""
        best_pos = None
        best_score = float('inf')
        
        for start_row in range(n):
            for start_col in range(m):
                if can_place_piece(grid, shape, start_row, start_col):
                    # Calculate score: prefer positions that create compact arrangements
                    # Lower row + lower column = better (top-left preference)
                    # Also consider adjacency to existing pieces
                    score = start_row * m + start_col
                    
                    # Bonus for being adjacent to existing pieces
                    adjacency_bonus = 0
                    for dr, dc in shape:
                        r, c = start_row + dr, start_col + dc
                        # Check adjacent cells
                        for ar, ac in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                            if 0 <= ar < n and 0 <= ac < m and grid[ar][ac] != 0:
                                adjacency_bonus -= 5  # Lower score is better
                    
                    final_score = score + adjacency_bonus
                    
                    if final_score < best_score:
                        best_score = final_score
                        best_pos = (start_row, start_col)
        
        return best_pos
    
    # Place pieces with smart positioning
    for piece_num, block_type in enumerate(figure, 1):
        if block_type not in shapes:
            continue
            
        shape = shapes[block_type]
        pos = get_best_position(grid, shape)
        
        if pos:
            place_piece(grid, shape, pos[0], pos[1], piece_num)
    
    return grid

# Test function
def test_solution():
    """Test the solution with the given example"""
    result = solution(4, 4, ['D', 'B', 'A', 'C'])
    
    print("Result for n=4, m=4, figure=['D','B','A','C']:")
    for row in result:
        print(row)
    
    print("\nExpected result:")
    expected = [
        [1, 2, 2, 2],
        [1, 1, 3, 0],
        [1, 4, 4, 0],
        [0, 4, 4, 0]
    ]
    for row in expected:
        print(row)
    
    return result

# Run test
if __name__ == "__main__":
    test_solution()