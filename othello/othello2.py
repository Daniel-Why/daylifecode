import random
import time
'''
- 落点周围没有棋子不能落子
- 落点周围的数字都相同不能落子
- 落子后8个方向移动，两个相同子之间的子翻转为相同颜色
- 最后统计那个颜色的子多
'''
# 创建玩家
def create_player():
    player_dict={"player_01":1,"player_02":2}
    return player_dict

class Player:
    name = ""
    player_id = 0
    def __init__(self,name,player_id,player_type = "human"):
        self.name = name
        self.player_id = player_id
        self.player_type = player_type
        self.player_status = "undo"


    # 输入落子的坐标
    def move_input(self,can_move_piece_check_list = []):
        if self.player_type == "human":
            piece_pointer = []
            x,y = map(int,input('请输入落子的坐标，以\",\"分割：').split(","))
            piece_pointer.append(x)
            piece_pointer.append(y)
        elif self.player_type == "AI":
            time.sleep(2)
            piece_pointer = random.choice(can_move_piece_check_list)
        print("落子:",piece_pointer)        
        return piece_pointer

# 创建棋盘
def create_othello_board(size = 8):
    # 自动生成满足尺寸的棋盘 # 输入超出范围的坐标的处理
    
    if size % 2 == 0:
        board= []
        board_row = size *[0]
        for i in range(0,size):
            board_row_copy = board_row.copy()
            board.append(board_row_copy)
        board[size//2-1][size//2-1]=2
        board[size//2][size//2]=2
        board[size//2-1][size//2]=1
        board[size//2][size//2-1]=1
    else:
        print("棋盘尺寸应该为偶数！")

    #board = [
    #    [0,0,0,0,0,0,0,0],
    #    [0,0,0,2,0,0,0,0],
    #    [0,0,0,0,2,2,1,0],
    #    [0,0,0,2,2,0,0,0],
    #    [0,0,0,1,2,0,0,0],
    #    [0,0,0,0,0,1,0,0],
    #    [0,0,0,0,0,0,0,0],
    #    [0,0,0,0,0,0,0,0]
    #    ]

    # board = [[1,2,3],[4,5,6],[7,8,9]]
    
    # board =[
    #         [2, 2, 2, 1],
    #         [2, 2, 2, 1],
    #         [2, 2, 2, 1],
    #         [2, 2, 2, 0]
    #     ]

    return board

# 打印棋盘
def board_print(board): 
    for i in board :
        print(i)

#piece_pointer 落子位置，direction 移动方向，step_length 每次移动步长
def move_pointer(piece_pointer,direction,step_length=1):
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

#限定落子后可以移动的方向
def move_direction(board,piece_pointer): 
        #设定边界
    board_len = len(board)
    move_direction_list = ["north","north-east","east","south-east","south","south-west","west","north-west"]
    if piece_pointer[1] == 0 and piece_pointer[0] != 0 and piece_pointer[0] != board_len-1:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north")
        move_direction_list.remove("north-east")
    if piece_pointer[1] == board_len-1 and piece_pointer[0] != 0 and piece_pointer[0] != board_len-1:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south")
        move_direction_list.remove("south-east")
    if piece_pointer[0] == 0 and piece_pointer[1] != 0 and piece_pointer[1] != board_len-1:
        move_direction_list.remove("north-west")
        move_direction_list.remove("west")
        move_direction_list.remove("south-west")
    if piece_pointer[0] == board_len-1 and piece_pointer[1] != 0 and piece_pointer[1] != board_len-1:
        move_direction_list.remove("south-east")
        move_direction_list.remove("east")
        move_direction_list.remove("north-east")
    if piece_pointer == [0,0]:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north-east")
        move_direction_list.remove("north")
        move_direction_list.remove("west") 
        move_direction_list.remove("south-west") 
    if piece_pointer == [board_len-1,0]:
        move_direction_list.remove("north-west")
        move_direction_list.remove("north-east")
        move_direction_list.remove("north")
        move_direction_list.remove("east") 
        move_direction_list.remove("south-east") 
    if piece_pointer == [0,board_len-1]:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south-east")
        move_direction_list.remove("south")
        move_direction_list.remove("west") 
        move_direction_list.remove("north-west") 
    if piece_pointer == [board_len-1,board_len-1]:
        move_direction_list.remove("south-west")
        move_direction_list.remove("south-east")
        move_direction_list.remove("south")
        move_direction_list.remove("east") 
        move_direction_list.remove("north-east")
    return move_direction_list

# 检查棋子是否超过边界：
def boundary_check(board,piece_pointer):
    return piece_pointer[1] < len(board) and piece_pointer[0] < len(board) and piece_pointer[1] >=0 and piece_pointer[0] >=0

# 落子后，四周可以翻转的棋子坐标
def move_piece(board,piece_pointer,player):
    if player.player_id == 1:
        opponent_id = 2
    elif player.player_id == 2:
        opponent_id = 1
    move_direction_list = move_direction(board,piece_pointer)
    # 判定落子周围是否有对手的子
    around_piece_list = []
    # print(move_direction_list)
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
        while board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] != 0 and board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] != player.player_id and boundary_check(board,piece_check_pointer_2) : # piece_check_pointer_2[1] < len(board) and piece_check_pointer_2[0] < len(board) and piece_check_pointer_2[1] >=0 and piece_check_pointer_2[0] >=0: 
            piece_check_pointer_2 = move_pointer(piece_pointer,i,step_length=step_len)
            if board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] == opponent_id:
                piece_check_pointer_2_list.append(piece_check_pointer_2)
            step_len = step_len + 1
            piece_check_pointer_3 = move_pointer(piece_pointer,i,step_length=step_len) # 用piece_check_pointer_3 假设检验 piece_pointer 移动后，piece_check_pointer_2 是否可能超出范围
            if  boundary_check(board,piece_check_pointer_3): # piece_check_pointer_3[1] < len(board) and piece_check_pointer_3[0] < len(board) and piece_check_pointer_3[1] >=0 and piece_check_pointer_3[0] >=0: #边界判断
                continue
            else:
                break
        if board[piece_check_pointer_2[1]][piece_check_pointer_2[0]] == player.player_id and boundary_check(board,piece_check_pointer_2): # piece_check_pointer_2[1] >=0 and piece_check_pointer_2[0] >=0:
            for n in piece_check_pointer_2_list:
                can_reverse_piece_pointer_list.append(n)
    if can_reverse_piece_pointer_list != []:
        can_reverse_piece_pointer_list.insert(0,piece_pointer)
    return can_reverse_piece_pointer_list #需要翻转的棋子列表

# 根据坐标翻转一枚棋子
def reverse_piece(board,piece_pointer,player):
    board[piece_pointer[1]][piece_pointer[0]] = player.player_id 

# 一次落子后，翻转所有可以翻转的棋子
def one_reversing(board,piece_pointer,player):# 一次落子
    # can_reverse_piece_pointer_list = ["start"]
    can_reverse_piece_pointer_list = move_piece(board,piece_pointer,player)
    if can_reverse_piece_pointer_list != []:
        for i in can_reverse_piece_pointer_list:
            reverse_piece(board,i,player)
        can_reverse_piece_pointer_list.remove(piece_pointer)

        for n in can_reverse_piece_pointer_list: # -----[2,3]
            one_reversing(board,n,player)

# 玩家完成一次落子
def one_play(board,piece_pointer,player):
    can_reverse_piece_pointer_list = move_piece(board,piece_pointer,player = player)
    if can_reverse_piece_pointer_list != [] and board[piece_pointer[1]][piece_pointer[0]] == 0:
        one_reversing(board,piece_pointer,player)
        print("完成一次落子".center(20,"—"))
        board_print(board)    
    else:
        # print(can_reverse_piece_pointer_list)
        print("不能在这里落子")
        print("请重新落子".center(20,"—"))
        board_print(board)
        can_move_piece_check_list = board_check(board,player)
        print("可以落子的地方：",can_move_piece_check_list)
        piece_pointer=player.move_input(can_move_piece_check_list)
        one_play(board,piece_pointer,player)

# 交换玩家
def player_change(now_player,player_01,player_02):
    if now_player.player_id == player_01.player_id:
        next_player = player_02
    elif now_player.player_id == player_02.player_id:
        next_player = player_01    
    return next_player


# 计算棋盘上的棋子
def piece_count(board,piece_id):
    piece_num = 0
    for i in board:
        piece_num = piece_num + i.count(piece_id)
    return piece_num

# 查看是否有可以走的棋
def board_check(board,player):
    # 用循环遍历棋盘上每个点
    check_board = board.copy()
    check_piece_list = []
    check_piece = [0,0]
    y = 0
    for i in check_board:
        check_piece[1] = y
        # print("y=",y)
        x = 0
        for n in i:
            check_piece[0] = x
            check_piece_list.append(check_piece.copy()) # 若 append check_piece，则列表会变为 [check_piece,check_piece,...,check_piece]，若check_piece 变化，列表中的所有值会跟着边，则会出现全部重复的项。
            x = x+1
        y = y + 1
    # print(check_piece_list)
    can_move_piece_check_list=[]
    # 确定每个点是否可以落子
    for m in check_piece_list:
        can_reverse_piece_pointer_check_list = move_piece(check_board,m,player)
        if can_reverse_piece_pointer_check_list != [] and check_board[m[1]][m[0]] == 0:
             can_move_piece_check_list.append(m.copy())
    return can_move_piece_check_list

    


# 开始游戏
def start_game(board):
    player_01 = Player("Daniel",1,"AI")
    player_02 = Player("Monna",2,"AI")
    overcheck = 0
    now_player = player_01
    while piece_count(board,0) != 0 and overcheck != 2:
        print("请玩家 {} 落子".format(now_player.name))
        can_move_piece_check_list = board_check(board,now_player)
        if can_move_piece_check_list != []:
            print("可以落子的地方：",can_move_piece_check_list)
            piece_pointer=now_player.move_input(can_move_piece_check_list)
            one_play(board,piece_pointer,now_player)
        elif can_move_piece_check_list == []:
            print("无法落子，交换选手！")
        now_player = player_change(now_player,player_01,player_02)
    print("对局结束".center(20,"—"))
    if piece_count(board,player_02.player_id) > piece_count(board,player_01.player_id):
        print("玩家 {} 胜利！".format(player_02.name))
    elif piece_count(board,player_02.player_id) < piece_count(board,player_01.player_id):
        print("玩家 {} 胜利！".format(player_01.name))
    else:
        print("平局！")

def main():
    board = create_othello_board(size=8)
    board_print(board)
    start_game(board)

main()
