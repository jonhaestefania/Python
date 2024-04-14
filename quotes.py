"""
To avoid suntax errors with strings Python has no trouble 
reading apostrophe inside double quotes. However, if you try 
to write a long message that includes a single apostrophe 
enclosed using sigle quotes Python interpreter issues an error message.
"""

message = "The Python's language maker is Guido Van Rossum"
print(message) # correct message wrote inside double quotes

message = 'The Python's language maker is Guido Van Rossum'
print(message) # The interpreter don't recognize this syntax
