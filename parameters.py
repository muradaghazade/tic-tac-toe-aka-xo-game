class Gameschema:
    def __init__(self):
        self.params = {"p1": " ", "p2": " ", "p3": " ", "p4": " ", "p5": " ", "p6": " ", "p7": " ", "p8": " ", "p9": " "}
        self.player = '2'
        self.play = True
        
    def get_input(self):
        self.commands_list = []
        command = input("Player 1: Enter your symbol:\t")
        command_2 = input("Player 2: Enter your symbol:\t")
        self.commands_list.append(command)
        self.commands_list.append(command_2)
        return self.commands_list
    
    def get_col(self):
        col = input("Enter the place: ('exit' to exit)\t")
        if col == 'exit':
            self.play = False
        return col

    def validate_command(self):
        # self.commands = self.get_input()
        self.col = self.get_col()
        if self.player == '1':
            self.params[self.col] = self.commands_list[0]
        else:
            self.params[self.col] = self.commands_list[1]
        return self.params

    def find_player(self):
        if self.player == '2':
            self.player = '1'
        else:
            self.player = '2'
        print(f'\nPlayer {self.player}s turn.\n')
        return self.player

    def find_winner(self):
        if self.params["p1"]==self.params["p2"]==self.params["p3"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p5"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p3"]==self.params["p5"]==self.params["p7"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p3"]==self.params["p6"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p4"]==self.params["p7"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p7"]==self.params["p8"]==self.params["p9"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p2"]==self.params["p5"]==self.params["p8"]=="x":
            print("\nPLAYER 1 WINS!\n")
        elif self.params["p1"]==self.params["p2"]==self.params["p3"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p1"]==self.params["p5"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p3"]==self.params["p5"]==self.params["p7"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p3"]==self.params["p6"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p1"]==self.params["p4"]==self.params["p7"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p7"]==self.params["p8"]==self.params["p9"]=="o":
            print("\nPLAYER 2 WINS!\n")
        elif self.params["p2"]==self.params["p5"]==self.params["p8"]=="o":
            print("\nPLAYER 2 WINS!\n")
        else:
            return self.params
        for param in self.params:
            self.params[param] = " "

    def show_result(self):
        print(f'  {self.params["p1"]} | {self.params["p2"]} | {self.params["p3"]}')
        print("-------------")
        print(f'  {self.params["p4"]} | {self.params["p5"]} | {self.params["p6"]}')
        print("-------------")
        print(f'  {self.params["p7"]} | {self.params["p8"]} | {self.params["p9"]}')
