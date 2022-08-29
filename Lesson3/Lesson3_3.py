omnivore = {'Steven Armstrong', 'Vasya Pupkin', 'Ostap Bender', 'Mary Sue'}
vegetarian = {'Jonh Miller', 'Steven Armstrong', 'Samuel Rodriguez', 'Tanaka Tarou'}

vegetable_eaters = omnivore.union(vegetarian)
# Same string. Solutions?
print(f'People that can eat vegetables: {vegetable_eaters}')