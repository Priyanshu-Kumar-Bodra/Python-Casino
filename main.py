print('WELCOME TO THE CASINO','\n', sep='\n')

while True:
      print('''What would you like to play?
            A: Slot Machine
            B: Roulette Table
            C: Exit''')
      opt = input('Enter an option: ')

      valid = 'ABCabc'
      if opt not in valid:
            print('Please enter a valid option')
            continue

      if opt.lower() == 'a':
            import slot_machine
      elif opt.lower() == 'b':
            print('Sorry, it is not available yet.')
      elif opt.lower() == 'c':
            break

print('THANKS FOR VISITING')

