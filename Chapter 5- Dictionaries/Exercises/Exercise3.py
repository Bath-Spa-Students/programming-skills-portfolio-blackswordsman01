#Glossary2
glossary = {
    'string': 'A collection of alphabets, words, or other characters.',
    'comment': 'Short descriptions along with the code to increase its readability.',
    'loop': 'Repeating something over and over until a particular condition is satisfied',
    'list': 'A data structure in Python that is a mutable, or changeable, ordered sequence of elements. ',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }
for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)