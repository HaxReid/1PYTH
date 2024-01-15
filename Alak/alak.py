def newBoard(n):
    board=[0]*n 
    return board   

def display(board, n):
    for i in range(n):
        if i>=9:
            print(" ", end="")
        if board[i]==0:
            print(".", end=" ")
        elif board[i]==1:
            print("x", end=" ")
        else: 
            print("o", end=" ")
    print()        
    for i in range(n):
        print(i+1,end=" ")


def possible(board,n,player,removed,i):
    return 0<=i<=n-1 and board[i]==0 and removed[player-1][i]!=player 
        
def changeJoueur(player):
    if player==1:
        return 2
    else:
        return 1

def select(board,n,player,removed):
    i=eval(input("quel pion choisir ? "))-1
    if possible(board,n,player,removed,i) is True:
        return i
    else:
        select(board,n,player,removed)
        
        
def put(board,n,player,removed,i):
    if possible(board,n,player,removed,i) != False:
        board[i] = player
    indexsuivant=i+1
    indexprecedent=i-1
    if i!=n-1 or (board[n-1]!=changeJoueur(player) and i==n-2):
        while board[indexsuivant] == changeJoueur(player):
            if indexsuivant == n-1:
                break
            else:
                indexsuivant+=1
        if indexsuivant<=n-1 and board[indexsuivant]==player:    
            for j in range(i+1,indexsuivant):
                board[j]=0   
    if i!=0 or (i==1 and board[0]!=changeJoueur(player)):                
        while board[indexprecedent] == changeJoueur(player):
            indexprecedent-=1
        if indexprecedent>=0 and board[indexprecedent]==player:    
            for j in range(i-1,indexprecedent,-1):
                board[j]=0    
    removed[player-1]=board
             
            
def again(board,n,player,removed):
    for i in range(n):
        if possible(board, n,player,removed,i)==True:
            return True
    return False


def win(board,n):
    joueur1=0
    joueur2=0
    for i in range(n):
        if i==1:
            joueur1+=1
        else:
            joueur2+=1
    if joueur1<joueur2:
        print("Joueur2 a gagné")
    elif joueur1>joueur2:
        print("Joueur1 a gagné")
    else:
        print("Egalité")

def alak(n):
    board=newBoard(n)
    display(board,n)
    removed=[]
    removed.append(board)
    removed.append(board)
    joueur=1
    while again(board,n,joueur,removed)==True:
        pion = select(board, n, joueur, removed)
        put(board,n,joueur,removed,pion)
        display(board,n)
        joueur=changeJoueur(joueur)
    win(board, n)    
            
alak(9)        
    
            
                    
            
        
        
        