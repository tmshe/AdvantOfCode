draw_lst = []
bingo_boards = [] 
wip_board = []
# with open("sample.txt",'r') as f: 
with open("input.txt",'r') as f: 
    for line in f: 
        line = line.strip()
        if len(draw_lst) == 0: 
            draw_lst = line.split(",")
            draw_lst = [int(i) for i in draw_lst]
        elif len(line) == 0: 
            if len(wip_board) > 0: 
                wip_board = [int(i) for i in wip_board]  
                bingo_boards.append(wip_board)          
                wip_board = list()
        else: 
            wip_board = wip_board + line.split()
wip_board = [int(i) for i in wip_board]
bingo_boards.append(wip_board) 

def CheckForWin(marked_idx): 
    # Check for win 
    mark_ct = 0 
    # check row
    row = 0
    while row < 5: 
        for idx in range(row * 5,row * 5 + 5):
            try:
                marked_idx.index(idx)
                mark_ct += 1 
            except: 
                break
        if mark_ct == 5: # Bingo!
            return True
        else: 
            mark_ct = 0
            row = row + 1 
            continue 
    # check col
    col = 0
    while col < 5: 
        for idx in range(col, col + 25, 5): 
            try:
                marked_idx.index(idx)
                mark_ct += 1
            except: 
                break
        if mark_ct == 5: # Bingo!
            return True
        else: 
            mark_ct = 0
            col = col + 1 
            continue 
    return False

# # ===== First to win =====
# marked_idx = []
# for i in range(0, len(bingo_boards)): 
#     marked_idx.append([])
# result = False 
# for round, draw in enumerate(draw_lst): # draw number 
#     if result == True: 
#         break 
#     for board_id, board in enumerate(bingo_boards): # mark on board 
#         try: 
#             marked_idx[board_id].append(board.index(draw))
#         except: # if draw number not found on board, move to the next board 
#             continue 
#         if len(marked_idx[board_id]) <= 4: # if less than 5 number marked on board, go to next board 
#             continue 
#         result = CheckForWin(marked_idx[board_id]) # check for win only more than 5 numbers marked 
#         if result == False: continue # no Bingo yet
#         if result == True: # Bingo! 
#             winning_round = round
#             winning_draw = draw
#             winning_board_id = board_id
#             winning_board = board
#             break 

# ===== Last to win =====
bingo_lst = []
drop_board_idx = []
marked_idx = []
for i in range(0, len(bingo_boards)): 
    marked_idx.append([])
result = False 
for round, draw in enumerate(draw_lst): # draw number 
    # if result == True: 
    #     break 
    for board_id, board in enumerate(bingo_boards): # mark on board 
        if board_id in drop_board_idx: 
            continue 
        try: 
            marked_idx[board_id].append(board.index(draw))
        except: # if draw number not found on board, move to the next board 
            continue 
        if len(marked_idx[board_id]) <= 4: # if less than 5 number marked on board, go to next board 
            continue 
        result = CheckForWin(marked_idx[board_id]) # check for win only more than 5 numbers marked 
        if result == False: continue # no Bingo yet
        if result == True: # Bingo! 
            winning_round = round
            winning_draw = draw
            winning_board_id = board_id
            winning_board = board
            # bingo_lst.append([winning_round, winning_draw, winning_board_id, winning_board])
            drop_board_idx.append(winning_board_id)
            continue # this board is done. 


for drop_idx in marked_idx[winning_board_id]: 
    try: 
        winning_board[drop_idx] = 0
    except: continue 

print("final score, {} * {} = {}".\
    format(sum(winning_board), winning_draw, sum(winning_board) * winning_draw))

print('end')