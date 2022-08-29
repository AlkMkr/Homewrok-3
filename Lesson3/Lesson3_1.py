Eleks = ['Jonh Miller', 'Mary Sue', 'Tanaka Tarou', 'Vasya Pupkin', 'Samuel Rodriguez']
Toshiba = ['Tanaka Tarou', 'Steven Armstrong', 'Vasya Pupkin', 'Ostap Bender']
Toshiba.extend(Eleks)
Eleks.clear()
print(f'List of employees of Toshiba + Eleks: {Toshiba}')