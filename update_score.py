def game():
    return 89


score=game()
with open('Score.txt') as f:
    highscore=int(f.read())
    
    if score> highscore:
        with open('Score.txt','w') as w:
            w.write(str(score))