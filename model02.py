d = {'key': 'value'}
print(d.get('key', 'default_value'))
print(d.get('key2', 'default_value'))


sequence = [1, 2, 3, 4, 5, 6]
filtered_values = [value for value in sequence if value != 6]

print(filtered_values)
