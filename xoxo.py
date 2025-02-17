def sum_three(a, b, c):
    return a + b + c

def print_board(xState, zState):
    board = [(f"\u001b[0;31m\u001b[1mX\u001b[0m" if xState[i] else (f"\u001b[0;32mO\u001b[0m" if zState[i] else str(i))) for i in range(9)]
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    
def check_win(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [0, 4, 8]]
    
    for win in wins:
        if sum_three(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match 🎉")
            return 1
        if sum_three(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match 🎉")
            return 0
    
    if sum(xState) + sum(zState) == 9:
        print("It's a draw! 🤝")
        return 2 
    
    return -1 

if __name__ == "__main__":
    xState = [0] * 9
    zState = [0] * 9
    turn = 1
    print("Welcome to Rivon Tic Tac Toe. 👋")

    while True:
        print_board(xState, zState)
        print("X's Turn" if turn == 1 else "O's Turn")

        while True:
            try:
                value = int(input("Please enter a value (0-8): "))
                if value < 0 or value > 8:
                    print("❌ Invalid input! Enter a number between 0 and 8.")
                elif xState[value] or zState[value]:
                    print("❌ Spot already taken! Choose another.")
                else:
                    break
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        winner = check_win(xState, zState)
        if winner != -1:
            print_board(xState, zState)
            print("Game Over! 🎮")
            break

        turn = 1 - turn