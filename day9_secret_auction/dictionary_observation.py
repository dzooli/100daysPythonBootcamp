import pprint
"""
    dictionary is a collection of key-value pairs
"""

my_dict = {'name1': 'value1', 'name2': 'value2'}
pprint.pprint(my_dict, compact=True)

issue_types = {
    'Bug': 'An issue with blocking results',
    'Task': 'Action to do more steps',
    'Improvement': 'A new or improved functionality',
    'Change Request': 'An user request available for voting'
}
pprint.pprint(issue_types)
print('')

try:
    print(issue_types['Epic'])
except KeyError:
    print('No such key in the dictionary')
    print('')

# Add new entry
issue_types['Epic'] = 'A bigger thing to finish'
pprint.pprint(issue_types)

print('')
print('Wiping the dictionary...')
issue_types = {}
print('Result:')
pprint.pprint(issue_types)

