#!/usr/bin/python3
""" N-queens puzzle """

import sys


def inboard(n):
    """Initializing chessboard """
    board = []
    [board.append([]) for a in range(n)]
    [horizontal.append(' ') for a in range(n) for horizontal in board]
    return (board)


def boardcopy(board):
    """copy of the chessboard """
    if isinstance(board, list):
        return list(map(boardcopy, board))
    return (board)


def solution_(board):
    """Will return the solution of chessboard """
    answer = []
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == "Q":
                answer.append([a], [b])
                break
    return (answer)


def outx(board, vat, hor):
    """point out spots on chessboard
    board (list): current board
    vat (int): vartical axis
    hor (int): horizontal axis
    """
    for h in range(hor + 1, len(board)):
        board[vat][h] = "#"
    for h in range(hor - 1, -1, -1):
        board[vat][h] = "#"

    for v in range(vat + 1, len(board)):
        board[v][hor] = "#"

    for v in range(vat - 1, -1, -1):
        board[v][vat] = "#"

    h = hor + 1
    for v in range(vat + 1, len(board)):
        if h >= len(board):
            break
        board[v][h] = "#"
        h += 1

    h = hor - 1
    for v in range(vat - 1, -1, -1):
        if h >= len(board):
            break
        board[v][h] = "#"
        h += 1
    h = hor - 1
    for v in range(vat + 1, len(board)):
        if h < 0:
            break
        board[v][h] = "#"
        h -= 1

    def recursive(board, var, queen, answer):
        """giving recusive  solution
        Args:
            board (list): working chessboard
            var (int): current number
            answer (list): lists of answer
        Returns:
            sluotions
        """
        if queen == len(board):
            answer.append(solution(board))
            return (answer)

        for a in range(len(board)):
            if board[var][a] == " ":
                t_board = boardcopy(board)
                t_board[var][a] = "Q"
                outx(t_board, var, a)
                answer = recursive(t_board, var + 1, gueen + 1, answer)
        return (answer)

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)

        board = inboard(int(sys.argv[1]))
        answer = recursive(board, 0, 0, [])
        for ans in answer:
            print(ans)
