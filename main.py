import re
from prettytable import PrettyTable

tokens = (
    'ID',
    'KEYWORD',
    'RELOP',
    'NUM',
    'LITERAL'
)

t_KEYWORD = 'UNION|INTERSECT|MINUS|TIMES|WHERE|LEFT\sJOIN|RIGHT\sJOIN|INNER\sJOIN|JOIN|DIVIDE\sBY|SEMIJOIN|SEMIMINUS'
t_ID = '[A-Za-z]{1}[\w]+'
t_RELOP = '[\<\>=]{1,2}'
t_NUM = '\s[0-9\.]+'
t_LITERAL = "\'[\w\s]+\'"

x = PrettyTable()
x.field_names = ['Токен', 'Лексема', 'Початок', 'Кінець', 'Довжина']

s = input('REAL > ')
# res_KEYWORD = re.findall(t_KEYWORD, s)
for k in re.finditer(t_KEYWORD, s):
    x.add_row(['KEYWORD', k[0], k.start(), k.end(), k.end() - k.start()])
    # print('KEYWORD', k[0], k.start(), k.end(), k.end() - k.start())
for k in re.finditer(t_ID, s):
    if not re.findall(t_KEYWORD, k[0]):
        x.add_row(['ID', k[0], k.start(), k.end(), k.end() - k.start()])
        # print('ID', k[0], k.start(), k.end(), k.end() - k.start())
for k in re.finditer(t_RELOP, s):
    x.add_row(['RELOP', k[0], k.start(), k.end(), k.end() - k.start()])
    # print('RELOP', k[0], k.start(), k.end(), k.end() - k.start())
for k in re.finditer(t_NUM, s):
    x.add_row(['NUM', k[0], k.start(), k.end(), k.end() - k.start() - 1])
    # print('NUM', k[0], k.start(), k.end(), k.end() - k.start())
for k in re.finditer(t_LITERAL, s):
    x.add_row(['LITERAL', k[0], k.start(), k.end(), k.end() - k.start()])
    # print('LITERAL', k[0], k.start(), k.end(), k.end() - k.start())
print(x.get_string())