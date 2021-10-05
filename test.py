
import chess

board = chess.Board('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(board)
while board.legal_moves != 0:
    #a = board.piece_map()   #where the piece is<a dictionary>
    a = board.legal_moves

    print(a)
    i = input('your current move')
    move = chess.Move.from_uci(str(board.parse_san(i)))
    board.push(move)
    print(board)
