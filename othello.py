'''
- 落点周围没有棋子不能落子
- 落点周围的数字都相同不能落子
- 落子后8个方向移动，两个相同子之间的子翻转为相同颜色
- 最后统计那个颜色的子多
'''
def create_othello_board():
    a = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    return a

def move_piece(person,x,y):
    pointer = [x,y]



print(b)
piece_A = 1
piece_B = 2
piece = piece_B
x = 1
y = 0
pointer = [x,y]
b[y][x] = 2
i = 1
while b[y+1][x] != piece and b[y+1][x] != 0:
    b[y+1][x] = 2
    y = y+1
print(b)
