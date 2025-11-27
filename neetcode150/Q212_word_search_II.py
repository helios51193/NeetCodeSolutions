
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        root = {}
        END = "*"

        # Generating the graph
        for w in words:
            cur = root
            for ch in w:
                cur = cur.setdefault(ch, {})
            
            cur[END] = w
        
        ROWS, COLS = len(board), len(board[0])
        res = []      

        def dfs(r,c,node):
            ch  = board[r][c]

            if ch not in node:
                return 

            nxt = node[ch]

            if "*" in nxt:
                res.append(nxt["*"])
                del nxt["*"]   # remove so we don't add twice
            
            board[r][c] = "#" # mark

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            
            board[r][c] = ch  # unmark

            if not nxt:
                del node[ch]
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
        
        return res
    
"""
    Last Looked
    27-11-25

""" 