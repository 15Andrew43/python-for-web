import re

def find_all_digits(text):
    exp = r'\d+'  #Тут напишите своё регулярное выражение  
    return re.findall(exp, text)

text = '1_2p3b45с6d'

print(find_all_digits(text))