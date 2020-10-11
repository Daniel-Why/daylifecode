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
        [0,0,0,2,2,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,0,0,1,0,0],
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

def move_piece(board,piece_pointer,player_id):
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
    if can_reverse_piece_pointer_list != []:
        can_reverse_piece_pointer_list.insert(0,piece_pointer)
    return can_reverse_piece_pointer_list #需要翻转的棋子列表


def reverse_piece(board,piece_pointer,player_id):#根据坐标翻转棋子
    board[piece_pointer[1]][piece_pointer[0]] = player_id 

def one_reversing(board,piece_pointer,player_id):# 一次落子
    # can_reverse_piece_pointer_list = ["start"]
    #print(piece_pointer) 
    can_reverse_piece_pointer_list = move_piece(board,piece_pointer,player_id = player_id)
    if can_reverse_piece_pointer_list != []:
        # print(can_reverse_piece_pointer_list)
        for i in can_reverse_piece_pointer_list:
            reverse_piece(board,i,player_id = player_id)
        can_reverse_piece_pointer_list.remove(piece_pointer)
        # board_print(board)
        # print(can_reverse_piece_pointer_list)
        for n in can_reverse_piece_pointer_list:
            one_reversing(board,n,player_id)

def one_play(board,piece_pointer,player_id):
    can_reverse_piece_pointer_list = move_piece(board,piece_pointer,player_id = player_id)
    if can_reverse_piece_pointer_list != []:
        one_reversing(board,piece_pointer,player_id)
    else:
        print("can not be moved")

def main():
    board = create_othello_board()
    board_print(board)
    player_id = 1
    piece_pointer = [3,2]
    one_play(board,piece_pointer,player_id = player_id)
    print("完成一次落子".center(20,"—"))
    board_print(board)
main()
