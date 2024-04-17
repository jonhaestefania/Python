# The get() method is used to pass the value when a key
# doesn't exist in the dictionary.

trailer = {'plate': 123abc, 'size': 48, 'model': 2022}
# print(trailer['carrier']) this statement raise an error

# to fix this error
trailer = {'plate': '123abc', 'size': 48, 'model': 2022}
carrier = trailer.get('carrier', 'This trailer has no carrier assigned.')

print(carrier)


