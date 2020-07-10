#!/usr/bin/env python
# coding: utf-8

# # Tic Tac Toe code

# First, I make a list to include all X and O values.

# In[1]:


l = [' 'for x in range(9)]


# Then, I set up the board to be displayed while playing

# In[2]:


from IPython.display import clear_output
def board():
    clear_output()
    print(l[0],'|',l[1],'|',l[2])
    print('-','+','-','+','-')
    print(l[3],'|',l[4],'|',l[5])
    print('-','+','-','+','-')
    print(l[6],'|',l[7],'|',l[8])


# By importing clear_output from IPython.display, I make sure there is not a board per move.

# Then, I define the input for both X and O

# In[5]:


def move_X():
    print ('Player 1 make your move')
    index = int(input())-1
    if l[index]=='X':
        print ('You have already played this move!, Try again')
        move_X()
    elif l[index]=='O':
        print ('Invalid move, Try again')
        move_X()
    else:
        l[index]='X'


# In[6]:


def move_O():
    print ('Player 2 make your move')
    index = int(input())-1
    if l[index]=='O':
        print ('You have already played this move!, Try again')
        move_O()
    elif l[index]=='X':
        print ('Invalid move, Try again')
        move_O()
    else:
        l[index]='O'


# I decreased the input by 1 to match the index of the list i created so that anyone who does not know about indexing or python in general can also play.

# Then, I assign the conditions for win for X and O seperately as I felt uncomfortable making 1 that works for both.

# In[7]:


def win_X():
    if l[0]=='X'and l[1]=='X' and l[2]=='X':
        return True
    elif l[3]=='X'and l[4]=='X' and l[5]=='X':
        return True
    elif l[6]=='X'and l[7]=='X' and l[8]=='X':
        return True
    elif l[0]=='X'and l[3]=='X' and l[6]=='X':
        return True
    elif l[1]=='X'and l[4]=='X' and l[7]=='X':
        return True
    elif l[2]=='X'and l[5]=='X' and l[8]=='X':
        return True
    elif l[0]=='X'and l[4]=='X' and l[8]=='X':
        return True
    elif l[2]=='X'and l[4]=='X' and l[6]=='X':
        return True


# In[8]:


def win_O():
    if l[0]=='O'and l[1]=='O' and l[2]=='O':
        return True
    elif l[3]=='O'and l[4]=='O' and l[5]=='O':
        return True
    elif l[6]=='O'and l[7]=='O' and l[8]=='O':
        return True
    elif l[0]=='O'and l[3]=='O' and l[6]=='O':
        return True
    elif l[1]=='O'and l[4]=='O' and l[7]=='O':
        return True
    elif l[2]=='O'and l[5]=='O' and l[8]=='O':
        return True
    elif l[0]=='O'and l[4]=='O' and l[8]=='O':
        return True
    elif l[2]=='O'and l[4]=='O' and l[6]=='O':
        return True


# Then, I assigned a functions that calculates draw outcomes.

# In[9]:


def draw():
    for i in range(9):
        if l[i]==' ':
            return False
    return True


# I also assigned a code for replay to make replaying easier.

# In[10]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# At last, using all the functions I made, I assembled the final product.

# In[12]:


while True:
    game=True
    l = [' 'for x in range(9)]
    while game:
        board()
        move_X()
        board()
        if win_X():
            print ('X, you won')
            game=False
            break
        else:
            if draw():
                board()
                print('draw')
                break
            
        move_O()
        board()
        if win_O():
            print ('O, you won')
            game=False
            break
        else:
            if draw():
                board()
                print('draw')
                break
            else:
                continue
    if not replay():
        break


# In[ ]:




