'''
- 落点周围没有棋子不能落子
- 落点周围的数字都相同不能落子
- 落子后8个方向移动，两个相同子之间的子翻转为相同颜色
- 最后统计那个颜色的子多
'''
def create_player():
    player_dict={"player_01":1,"player_02":2}
    return player_dict

def create_othello_board(size = 8):
    # 自动生成满足尺寸的棋盘
    # if size % 2 == 0:
    #     board= []
    #     board_row = size *[0]
    #     for i in range(0,size):
    #         board_row_copy = board_row.copy()
    #         board.append(board_row_copy)
    #     board[size//2-1][size//2-1]=2
    #     board[size//2][size//2]=2
    #     board[size//2-1][size//2]=1
    #     board[size//2][size//2-1]=1
    # else:
    #     print("棋盘尺寸应该为偶数！")
    board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,2,0,0,0,0],
        [0,0,0,0,2,2,1,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
        ]

    # board = [[1,2,3],[4,5,6],[7,8,9]]
    return board
def board_print(board):
    for i in board :
        print(i)


def move_pointer(piece_pointer,direction,step_length=1):#piece_pointer 落子位置，direction 移动方向，step_length 每次移动步长
    piece_move_pointer = piece_pointer.copy()
    if direction == "north":
        piece_move_pointer[1] = piece_move_pointer[1]-step_length
    if direction == "south":
        piece_move_pointer[1] = piece_move_pointer[1]+step_length
    if direction == "west":
        piece_move_pointer[0] = piece_move_pointer[0]-step_length
    if direction == "east":
        piece_move_pointer[0] = piece_move_pointer[0]+step_length
    if direction == "north-west":
        piece_move_pointer[1] = piece_move_pointer[1]-step_length
        piece_move_pointer[0] = piece_move_pointer[0]-step_length
    if direction == "south-east":
        piece_move_pointer[1] = piece_move_pointer[1]+step_length
        piece_move_pointer[0] = piece_move_pointer[0]+step_length
    if direction == "north-east":
        piece_move_pointer[1] = piece_move_pointer[1]-step_length
        piece_move_pointer[0] = piece_move_pointer[0]+step_length
    if direction == "south-west":
        piece_move_pointer[1] = piece_move_pointer[1]+step_length
        piece_move_pointer[0] = piece_move_pointer[0]-step_length
    return piece_move_pointer

def move_direction(board,piece_pointer):
        #设定边界
    board_len = len(board)
    move_direction_list = ["north","north-east","east","south-east","south","south-west","west","north-west"]
    if piece_pointer[1] == 0 and piece_pointer[0] != 0 and piece_pointer[0] != board_len:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north")
        move_direction_list.remove("north-east")
    if piece_pointer[1] == board_len and piece_pointer[0] != 0 and piece_pointer[0] != board_len:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south")
        move_direction_list.remove("south-east")
    if piece_pointer[0] == 0 and piece_pointer[1] != 0 and piece_pointer[1] != board_len:
        move_direction_list.remove("north-west")
        move_direction_list.remove("west")
        move_direction_list.remove("south-west")
    if piece_pointer[0] == board_len and piece_pointer[1] != 0 and piece_pointer[1] != board_len:
        move_direction_list.remove("south-east")
        move_direction_list.remove("east")
        move_direction_list.remove("north-east")
    if piece_pointer == [0,0]:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north-east")
        move_direction_list.remove("north")
        move_direction_list.remove("west") 
        move_direction_list.remove("south-west") 
    if piece_pointer == [board_len,0]:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north-east")
        move_direction_list.remove("north")
        move_direction_list.remove("east") 
        move_direction_list.remove("south-east") 
    if piece_pointer == [0,board_len]:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south-east")
        move_direction_list.remove("south")
        move_direction_list.remove("west") 
        move_direction_list.remove("north-west") 
    if piece_pointer == [board_len,board_len]:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south-east")
        move_direction_list.remove("south")
        move_direction_list.remove("east") 
        move_direction_list.remove("north-east")
    return move_direction_list

def move_piece(board,piece_pointer,player_id = 1):
    if player_id == 1:
        opponent_id = 2
    elif player_id == 2:
        opponent_id = 1
    move_direction_list = move_direction(board,piece_pointer)
    # 判定落子周围是否有对手的子
    around_piece_list = []
    for i in move_direction_list:
        piece_check_pointer = move_pointer(piece_pointer,i)
        piece_id = board[piece_check_pointer[1]][piece_check_pointer[0]]
        around_piece_list.append(piece_id)

    if opponent_id in around_piece_list:
        print("Can be moved!")
    else:
        print("Can not be moved!")
    # print(around_piece_list)
    
    # 找到可以翻转子的方向
    move_piece_direction_list = []
    direct_num = around_piece_list.count(opponent_id)
    for i in range(0,direct_num):
        direct_index = around_piece_list.index(opponent_id)
        move_piece_direction_list.append(move_direction_list[direct_index])
        around_piece_list.remove(opponent_id)
        move_direction_list.remove(move_direction_list[direct_index])
    # print(move_piece_direction_list)

    # 找出每个方向可以反转的棋子
    can_reverse_piece_pointer_list = []
    for i in move_piece_direction_list:
        step_len = 1
        piece_check_pointer_2 = move_pointer(piece_pointer,i,step_length=step_len)
        piece_check_pointer_2_list = []
        # print(i,piece_check_pointer_2)
        while board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] != 0 and board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] != player_id: 
            piece_check_pointer_2 = move_pointer(piece_pointer,i,step_length=step_len)
            if board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] == opponent_id:
                piece_check_pointer_2_list.append(piece_check_pointer_2)
            step_len = step_len + 1
        if board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] == player_id:
            for n in piece_check_pointer_2_list:
                can_reverse_piece_pointer_list.append(n)
    can_reverse_piece_pointer_list.insert(0,piece_pointer)
    return can_reverse_piece_pointer_list

def reverse_piece(board,piece_pointer):
    if board[piece_pointer[1]][piece_pointer[0]] == 1:
        board[piece_pointer[1]][piece_pointer[0]]=2
    else:
        board[piece_pointer[1]][piece_pointer[0]]=1
    return board

def main():
    board = create_othello_board()
    board_print(board)
    piece_pointer = [3,2]
    can_reverse_piece_pointer_list = move_piece(board,piece_pointer)
    print(can_reverse_piece_pointer_list)
    for i in can_reverse_piece_pointer_list:
        reverse_piece(board,i)
    board_print(board)

main()



# print(b)
# piece_A = 1
# piece_B = 2
# piece = piece_B
# x = 1
# y = 0
# pointer = [x,y]
# b[y][x] = 2
# i = 1
# while b[y+1][x] != piece and b[y+1][x] != 0:
#     b[y+1][x] = 2
#     y = y+1
# print(b)
