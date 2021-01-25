issue_types = {
    'Bug': 'An issue with blocking results',
    'Task': 'Action to do more steps',
    'Improvement': 'A new or improved functionality',
    'Change Request': 'An user request available for voting'
}

print('Keys:')
print(issue_types.keys())

print('Values:')
print(issue_types.values())

print('Keys and Values as a list of 2 element tuples:')
print(issue_types.items())

print('')
print('Looping through...')
for dkey in issue_types:
    print('Key is:', dkey + ';', 'Value:', issue_types[dkey])

print('')
print('Retrieve and remove the element with popitem() as an 1-element dictionary')
item = issue_types.popitem()
print(item)
print(issue_types)

print('')
print('Retrieve and remove an element value with pop() [Key: \'Bug\']')
itemvalue = issue_types.pop('Bug')
print(itemvalue)
print(issue_types)