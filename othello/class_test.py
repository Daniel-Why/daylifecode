class board:
    # 创建棋盘
    def __init__(self,size = 8):
        board = []
        # 自动生成满足尺寸的棋盘 # 输入超出范围的坐标的处理
        if size % 2 == 0:
            self.board= []
            board_row = size *[0]
            for i in range(0,size):
                board_row_copy = board_row.copy()
                self.board.append(board_row_copy)
            self.board[size//2-1][size//2-1]=2
            self.board[size//2][size//2]=2
            self.board[size//2-1][size//2]=1
            self.board[size//2][size//2-1]=1
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

    # 打印棋盘
    def board_print(self): 
        for i in self.board :
            print(i)
class player:
    name = ""
    player_id = 0
    def __init__(self,name,player_id):
        self.name = name
        self.player_id = player_id


class test2:
    def __init__(self):
        print("我是 test2")
        self.me = "apple"
        print(self.me)

    def shenfa(self,a,b):
        c = a * b
        return c

class test(test2):
    def __init__(self,a,b):
        d = self.jiafa(a,b)
        shenfa = test2()
        e = shenfa.shenfa(a,b)
        print("a+b=",d)
        print("a*b=",e)

    def jiafa(self,a,b):
        c = a + b
        return c


a = board(4)
a.board_print()
player01 = player("daniel",1)
print(player01.player_id)
b=a.board.copy()
print(b)

test(2,3)
a = test2()
print("a.me=",a.me)
a.me = "coconut"
print("new_a.me=",a.me)