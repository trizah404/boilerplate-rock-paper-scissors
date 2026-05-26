def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    counter = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) < 3:
        return "R"

    pattern = "".join(opponent_history[-3:])
    
    play_counts = {"R": 0, "P": 0, "S": 0}
    
    for i in range(len(opponent_history) - 3):
        if "".join(opponent_history[i:i+3]) == pattern:
            next_play = opponent_history[i+3] if i+3 < len(opponent_history) else None
            if next_play:
                play_counts[next_play] += 1

    predicted = max(play_counts, key=play_counts.get)

    return counter[predicted]