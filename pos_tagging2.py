# Contoh pos tagging untuk kata-kata dalam aturan produksi CNF
pos_tags = {
    'S': 'saya Putra batu hari tiga itu',
    'P': 'saya Putra batu hari tiga itu kerja pergi terbang loncat makan',
    'Ket': 'Prep saya Putra batu hari tiga itu',
    'L1': 'saya Putra batu hari tiga itu Noun',
    'O': 'saya Putra batu hari tiga itu Noun',
    'Pel': 'saya Putra batu hari tiga itu Adj',
    'L2': 'Adj saya Putra batu hari tiga itu',
    'L3': 'Adj saya Putra batu hari tiga itu',
    'L4': 'saya Putra batu hari tiga itu Noun',
    'NP': 'Det saya Putra batu hari tiga itu',
    'VP': 'kerja pergi terbang loncat makan saya Putra batu hari tiga itu',
    'NumP': '1 2 3 satu saya Putra batu hari tiga itu',
    'Verb': 'kerja pergi terbang loncat makan',
    'Noun': 'saya Putra batu hari tiga itu',
    'Prep': 'di ke dari untuk pada',
    'Adj': 'sedih marah',
    'Adv': 'kurang banyak',
    'Num': '1 2 3 satu'
}


# Kalimat contoh
sentence = "saya makan"

# Melakukan tokenisasi kata-kata dalam kalimat
words = sentence.split()

# Melakukan pos tagging berdasarkan aturan produksi CNF
for word in words:
    for key, value in pos_tags.items():
        if word in value.split():
            print(f"{word} memiliki pos tag {key}")
