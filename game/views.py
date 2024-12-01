from django.shortcuts import render
from django.http import JsonResponse
from .game_logic import Board
from .go import Board
# In-memory board storage for simplicity
current_board = Board()

def new_game(request):
    global current_board
    current_board = Board()
    return JsonResponse(current_board.to_dict())

def board_state_view(request):
    board = Board()
    board_state = board.to_dict()
    return JsonResponse(board_state)

def make_move(request):
    global current_board
    x, y = int(request.GET['x']), int(request.GET['y'])
    move_made = current_board.put_stone((x, y), check_legal=True)
    if not move_made:
        return JsonResponse({'error': 'Illegal move'}, status=400)
    return JsonResponse(current_board.to_dict())
