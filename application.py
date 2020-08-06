from parameters import Gameschema


class Application:
    def run(self):
        game = Gameschema()
        game.get_input()
        while game.play == True:
            game.find_player()
            game.validate_command()
            game.show_result()
            game.find_winner()

welcome = 'WELCOME TO TIC-TAC-TOE!'

print('\n\t\t\t-----------------------\n')
print(f'\t\t\t{welcome}')
print('\n\t\t\t-----------------------\n')
print(f'\n  p1 | p2 | p3')
print("----------------")
print(f'  p4 | p5 | p6')
print("----------------")
print(f'  p7 | p8 | p9\n')

app = Application()
app.run()