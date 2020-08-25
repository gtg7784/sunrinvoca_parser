# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from tqdm import tqdm
import json

data = pd.read_excel('./voca.xlsx')
data = data.astype(object).replace(np.nan, None)

print(data)

result = []

for index, day in enumerate(tqdm(data['일자'])):
  if day is None:
    break

  if 'DAY' not in day:
    break

  day_no = int(day[3:])
  word = data['표제어'][index]
  meaning = data['어휘 뜻'][index]
  description = data['description'][index]

  if True not in [day_no == i['day'] for i in result] or [] == [day_no == i['day'] for i in result]:
    result.append({
      'day': day_no,
      'description': description if None is not description else '',
      'word': [word],
      'meaning': [meaning]
    })

  else:
    result[day_no - 1]['word'].append(word)
    result[day_no - 1]['meaning'].append(meaning)


with open("words.json", "w") as f:
  json.dump(result, f)
