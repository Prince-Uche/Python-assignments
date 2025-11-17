user_age = int(input('Enter your age: '))

print('Your maximum heart rate is = ', 220 - user_age, 'bpm')

print ('Your target heart rate range is', (220 - user_age) * 0.50, 'to', (220 - user_age) * 0.85, 'bpm')

