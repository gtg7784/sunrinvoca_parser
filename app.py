# -*- coding:utf-8 -*-

import pandas as pd
import json

data = pd.read_excel('./voca.xlsx')

print(data)

result = []

for index, day in enumerate(data['일자']):
  if day is None:
    print('item is None')
    break

  if 'DAY' not in day:
    print('일자가 아닙니다.')
    break

  day_no = int(day[3:])
  word = data['표제어'][index]
  meaning = data['어휘 뜻'][index]

  if True not in [day_no == i['day'] for i in result] or [] == [day_no == i['day'] for i in result]:
    result.append({
      'day': day_no,
      'description': '',
      'word': [word],
      'meaning': [meaning]
    })
  else:
    result[day_no - 1]['word'].append(word)
    result[day_no - 1]['meaning'].append(meaning)


with open("words.json", "w") as f:
  json.dump(result, f)

  