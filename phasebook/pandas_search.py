import pandas as pd

from data.search_data import USERS

df = pd.DataFrame(USERS)

search_criteria = {
  #"id": "5",
  #"name": "Joe",
  "age": 28,
  #"occupation": "Arc"
}

# compose our filter
query_param = ""
for criteria in search_criteria:
    if(len(query_param)):
        query_param += " | "
    if criteria == 'id':
        query_param += '(id == %s)' % (search_criteria['id'])
    if criteria == 'age':
        age = search_criteria['age']
        query_param += '(age >= %d & age <= %d)' % (age - 1, age + 1)
    if criteria == 'name':
        query_param += 'name.str.contains("%s")' % (search_criteria['name'])
    if criteria == 'occupation':
        query_param += 'occupation.str.contains("%s")' % (search_criteria['occupation'])

if (len(query_param)):
    sdf = df.loc[df.query(query_param, engine='python').index]
    sdf = sdf.sort_values(by=['id', 'name', 'age', 'occupation'])
    print(sdf)
else:
    print(df)
