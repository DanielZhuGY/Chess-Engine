import chess
turn = 0
board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(board)
while board.legal_moves != 0:
    turn = turn +1
    print('{} round'.format(turn))
    b = board.piece_map()   #where the piece is<a dictionary>
    if turn%2 != 0:
        print('white turn')
    else:
        print('black turn')
    a = board.legal_moves

    print(a)
    i = input('your current move')
    move = chess.Move.from_uci(str(board.parse_san(i)))
    board.push(move)
    print(board)

