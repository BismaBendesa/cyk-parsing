grammar_rules = {
    'K': [
        ('S', 'P'),
        ('S', 'Ket'),
        ('L1', 'O'),
        ('L1', 'Pel'),
        ('L1', 'Ket'),
        ('L1', 'L2'),
        ('L1', 'L3'),
        ('L4', 'Ket')
    ],
    'L1': [
        ('S', 'P'),
    ],
    'L2': [
        ('Pel', 'Ket'),
        ('O', 'Ket')
    ],
    'L3': [
        ('O', 'Pel'),
    ],
    'L4': [
        ('L1', 'L3')
    ],
    'S': [
        ('NP', 'Noun'),
        ('NP', 'Adj'),
        ('NP', 'PropNoun'),
        ('Num', 'NP'),
        ('NP', 'Pronoun'),
        ('NP', 'Adv'),
        ('Adv', 'NP'),
        ('saya',),
        ('Putra',),
        ('batu',),
        ('hari',),
        ('tiga',),
        ('itu',)
    ],
    'P': [
        ('NP', 'Noun'),
        ('Adv', 'VP'),
        ('Adv', 'NP'),
        ('Prep', 'NP'),
        ('VP', 'Adj'),
        ('NP', 'Adj'),
        ('guru',),
        ('makan',),
        ('tidur',),
        ('marah',),
        ('di',)
    ],
    'O': [
        ('NP', 'Noun'),
        ('NP', 'Adj'),
        ('NP', 'PropNoun'),
        ('Num', 'NP'),
        ('NP', 'Pronoun'),
        ('NP', 'Adv'),
        ('Adv', 'NP'),
        ('saya',),
        ('Putra',),
        ('batu',),
        ('tiga',)
    ],
    'Pel': [
        ('NP', 'Noun'),
        ('NP', 'Adj'),
        ('Adv', 'Adj'),
        ('NP', 'PropNoun'),
        ('Num', 'NP'),
        ('NP', 'Pronoun'),
        ('NP', 'Adv'),
        ('Adv', 'NP'),
        ('saya',),
        ('Putra',),
        ('batu',),
        ('hari',),
        ('tiga',),
        ('sedih',)
    ],
    'Ket': [
        ('Prep', 'NP')
    ],
    'NP': [
        ('NP', 'Noun'),
        ('NP', 'Adj'),
        ('NP', 'PropNoun'),
        ('Num', 'NP'),
        ('NP', 'Pronoun'),
        ('NP', 'Adv'),
        ('Adv', 'NP'),
        ('saya',),
        ('Putra',),
        ('batu',),
        ('hari',),
        ('tiga',),
        ('itu',)
    ],
    'VP': [
        ('Adv', 'VP'),
        ('kerja',),
        ('pergi',),
        ('terbang',),
        ('loncat',),
        ('makan',)
    ],
    'NumP': [
        ('Num', 'NP'),
        ('1',),
        ('2',),
        ('3',),
        ('satu',)
    ]
}
