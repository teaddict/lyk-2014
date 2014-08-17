__author__ = 'schwappkopf'

my_dict = {'water': 'su', 'flower': 'cicek', 'bird': 'kus', 'life': 'hayat', 'watch': 'saat'}

while (True):
    word = str(raw_input("bir kelime girin: "))
    if word == "q":
            break

    print my_dict.get(word)


my_reverse=zip(my_dict.values(),my_dict.keys()) #tersden oluşturmak için
print my_reverse
