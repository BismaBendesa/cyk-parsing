startState = "K"
grammar = {
  startState:['S', 'P'],
  'S': [('NP', 'VP')],
  'NP': [('Noun',)],
  'VP': [('Verb',)],
  'Noun': ['John', 'Mary'],
  'Verb': ['plays', 'eats'],
}

# grammar_rules = {
#     'K': [('S', 'P')],
#     'S': [('NP', 'VP')],
#     'NP': [('Noun',)],
#     'VP': [('Verb',)],
# }