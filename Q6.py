#Q6. wap to check whether George's and Barbie's friendship is real

def func(word):
    if len(word)==1:
        return [word]
    partial_words=func(word[1:])
    char=word[0]
    result=[]
    for combo in partial_words:
        for i in range(len(combo)+1):
            result.append(combo[:i]+char+combo[i:])
    return result        


initial=input('Player 1: Enter initial word -> ').lower()
possible=func(initial)
guess=input('Player 2: Enter your guess -> ').lower()

if guess in possible:
    print('Friendship is real :)')
else:
    print('Friendship is fake :(')
