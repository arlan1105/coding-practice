def get_best_hand(cards):
    rank = sorted([card[0] for card in cards])
    suit = [card[1] for card in cards]
    rank_occurence = [rank.count(c) for c in set(rank)]
    suit_occurence = [suit.count(c) for c in set(suit)]
    rank_order = sorted(['A23456789TJQK'.index(c) for c in rank])
    is_consecutive = (rank_order == list(range(rank_order[0], rank_order[-1] + 1))) or (rank_order == list(range(rank_order[0], rank_order[-1] - 1, -1)))
    #if rank_order == [0, 9, 10, 11, 12]:
    #    is_consecutive = True
    is_flush = 5 in suit_occurence

    if is_flush and all(c in ["A", "K", "Q", "J", "T"] for c in rank):
        return 'Royal Flush'
    if is_flush and is_consecutive: 
        return 'Straight Flush'
    if 4 in rank_occurence: 
        return 'Four of a Kind'
    if 3 in rank_occurence and 2 in rank_occurence: 
        return 'Full House' 
    if is_flush: 
        return 'Flush'
    if is_consecutive: 
        return 'Straight'
    if rank_occurence.count(3) == 1: 
        return 'Three of a Kind'
    if rank_occurence.count(2) == 2: 
        return 'Two Pair'
    if rank_occurence.count(2) == 1: 
        return 'Pair'
    return 'High Card'

print(get_best_hand(["As", "Kh", "Jd", "8c", "5h"]))
print(get_best_hand(["Ts", "Th", "7c", "6d", "5h"]))
print(get_best_hand(["Ts", "Th", "9d", "9c", "8h"]))
print(get_best_hand(["7s", "7h", "7d", "2c", "5h"]))
print(get_best_hand(["As", "2h", "3d", "4c", "5h"]))
print(get_best_hand(["2h", "5h", "7h", "9h", "Jh"]))
print(get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]))
print(get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]))
print(get_best_hand(["8c", "9c", "7c", "6c", "5c"]))
print(get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]))
