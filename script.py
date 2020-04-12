from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Stacks Created
stacks = []
left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')
stacks += [left_stack, middle_stack, right_stack]


#Set up the Game
num_disks = int(input('\nHow many disks do you want to play with?\n'))

#Checks if num_discs is less than 3
while num_disks < 3:
  num_disks = int(input('Enter a number greater than or equal to 3\n'))

#Iterates backwards through range of num_discs
for disk in range(num_disks, 0, -1):
  left_stack.push(disk)
#left_stack.print_items()

#Calculates the number of optimal moves
num_optimal_moves = (2 ** num_disks) - 1
print('\nThe fastest you can solve this game is in {0} moves'.format(num_optimal_moves))


#Get User Input
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]

#Asks the user for a valid input until we get one thats valid by iterating through the stacks
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('Enter {0} for {1}'.format(letter, name))

    user_input = input('')

    if user_input in choices:
      for i in range(len(stacks)):
        return stacks[i]
       
#Play the Game
num_user_moves = 0

#Loops while the size of right_stack is not equal to num_discs
while(right_stack.get_size != num_disks):
  print('\n\n\n...Current Stacks...')
  for stack in stacks:
    stack.print_items

 #Asks the user what move they want to make until they make a valid move
  while True:
    print('\nWhich stack do you want to move from?\n')
    from_stack = get_input()
    print('\nWhich stack do you want to move to?\n')
    to_stack = get_input()

#If the user tries to move a disk from an empty stack the move will be invalid
    if from_stack.get_size == 0:
      print('\n\nInvalid Move. Try Again')

#if the user moves a disk to an empty stack or moves a disk onto a larger disk, thats a valid move     
    elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break

#If the user tries to move a larger disk onto a smaller disk the move is inlvalid
    else:
      print('\n\nInvalid Move. Try Again')

print('\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}'.format(num_user_moves, num_optimal_moves))
