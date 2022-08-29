vip_room = ('Steven Armstrong', 'Vasya Pupkin', 'Ostap Bender', 'Mary Sue')
ordinary_room = ['Jonh Miller', 'Steven Armstrong', 'Samuel Rodriguez', 'Tanaka Tarou', None]

ordinary_room[4] = str(input('Enter a name for open position:'))
print(f'Guests in common room: {ordinary_room}\nGuests in VIP room: {vip_room}')

