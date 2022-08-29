casino_blacklist = {'Tanaka Tarou', 'Steven Armstrong', 'Vasya Pupkin', 'Ostap Bender', 'Mary Sue'}
poker_blacklist = {'Tanaka Tarou', 'Steven Armstrong', 'Samuel Rodriguez', 'Mary Sue'}
alcohol_blacklist = {'Jonh Miller', 'Mary Sue', 'Tanaka Tarou', 'Vasya Pupkin', 'Samuel Rodriguez'}

blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
# Using string here because list is ugly in output with double parentheses. Other solutions?
print(f'Totally blacklisted guests: {blacklist}')

