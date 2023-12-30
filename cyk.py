# ... (previous code remains unchanged)
get_right_hand = []

def get_all_right_hand(dictionary_cnf, n):
    for i in range(0, n):
        for left_hand, rule in dictionary_cnf.items():
            for right_hand in rule:
                get_right_hand.append(right_hand)


def string_exist(string, n):
    for i in range(0, n):
        if string.split()[i] not in get_right_hand:
            return -1
    return 1

def filling_bottom(dictionary_cnf, input_text, table_filling, n):
    string_split = input_text.split()
    for i in range(0, n):
        for left_hand, rule in dictionary_cnf.items():
            for right_hand in rule:
                if len(right_hand.split()) == 1 and right_hand == string_split[i]:
                    table_filling[i][i].add(left_hand)


def filling_remaining(dictionary_cnf, table_filling, n):
    for i in range(0, n):
        for j in range(i, -1, -1):
            for k in range(j, i + 1):
                for left_hand, rule in dictionary_cnf.items():
                    for right_hand in rule:
                        if len(right_hand.split()) == 2 and right_hand.split()[0] in table_filling[j][k] and right_hand.split()[1] in table_filling[k + 1][i]:
                            table_filling[j][i].add(left_hand)

def is_accepted(dictionary_cnf, table_filling, flag, n):
    if list(dictionary_cnf.keys())[0] in table_filling[0][n - 1] and flag == 1:
        return ["valid", table_filling]
    elif flag == -1:
        return ["not_registered", table_filling]
    else:
        return ["invalid", table_filling]


def cyk(dictionary_cnf, input_text):
    n = len(input_text.split())
    table_filling = [[set([]) for j in range(n)] for i in range(n + 1)]
    get_all_right_hand(dictionary_cnf, n)
    flag = string_exist(input_text, n)
    filling_bottom(dictionary_cnf, input_text, table_filling, n)
    filling_remaining(dictionary_cnf, table_filling, n)
    return is_accepted(dictionary_cnf, table_filling, flag, n)

# Test Nomina
# -------------------------
# 48 | SP : Kamar tidur ini sangat nyaman (NP Pronoun adv adj) PASS ✅
# 49 | SP : Pertunjukan Teater ini sangat indah (NP Pronoun adv adj)



# Rules of the grammar
R = {
    'K': ['S P'],
    'Noun': ['Kamar', 'tidur'], 
    'NP': ['Num NP', 'NP Adj', 'NP Noun', 'NP Noun', 'NP Pronoun', 'NP PropNoun', 'NP Adv', 'NP Adv', 'Kamar', 'tidur'], 
    'Pronoun': ['ini'],
    'Adv': ['sangat'],
    'Adj':['nyaman'],
    "S": ['NP', 'Pronoun', 'PropNoun', 'Num NP', 'NP Adj','NP Noun', 'NP Pronoun', 'NP PropNoun', 'NP Adv', 'Adv NP', 'Noun',],
    "P" : ['NP', 'VP', 'Adv VP', 'Verb', 'PP', 'AdjP', 'Adv Adj','belajar', 'bermain', 'mengerjakan', 'meniru', 'mengendarai', 'minum', 'makan', 'main', 'mengetik', 'duduk', 'berdiri', 'toko', 'wanita', 'kopi', 'tugas', 'ujian', 'pendidikan', 'tanah', 'motor', 'mobil','alkohol', 'laptop', 'ikan', 'sandal', 'pensil', 'projek', 'vas', 'sepeda', 'gelas', 'piring', 'guru', 'polisi', 'aktor' ], 
    "Ket" : ['Prep NP', 'pasar', 'kebun', 'rumah', 'di sekolah', 'ke jepang', 'tanpa gula', 'dari bali', 'dengan senyum', 'untuk indonesia'], 
    "O" : ['NP', 'Num NP','Num','1','2','3','4','5','6','7','8','9','0', 'laptop', 'ikan', 'sandal', 'pensil', 'projek', 'vas', 'sepeda', 'gelas', 'piring','rumah',],
    "Pel": ['NP', 'AdjP', 'Num', 'Num NP', 'sapu', 'kertas', 'meja', 'foto', 'kaca', 'tembok', ], 
    "Prep" : ['di', 'ke', 'dari', 'pada'],
    "Num": ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'nol'], 
    'Verb' : ['belajar', 'bermain', 'mengerjakan', 'meniru', 'mengendarai', 'minum', 'makan', 'main', 'mengetik', 'duduk', 'berdiri', 'mancing'], 
    'PropNoun': ['Bob', 'Denpasar', 'Sungai Amazon']
}
string_input = "Kamar tidur ini sangat nyaman"
if cyk(R, string_input)[0] == 'valid':
  print("The sentence is Valid")
else: 
  if cyk(R, string_input)[0] == 'invalid':
      print("The sentence is Invalid")
  else:
      print("The sentence is not Registered")

