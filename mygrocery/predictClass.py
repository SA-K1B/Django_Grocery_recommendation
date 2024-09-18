import pandas as pd
class predictClass:
     def __init__(self,ruless):
       self.ruless=ruless
     def predict(self,cart):
      rules =  self.ruless
      recommend = []
      for ind,row in rules.iterrows():
        antecedents = set(row['antecedents'])
        consequents = set(row['consequents'])
        # print(antecedents)
        if antecedents.issubset(cart):
            recommend.append({
                'items':consequents,
                'confidence':row['confidence'],
                'lift':row['lift']
            })
      result = pd.DataFrame(recommend)
      result.sort_values('confidence',ascending=False)
      suggested = []
      for ind,row in result.iterrows():
        if row['lift'] > 1.5:
          suggested = row['items']
          break
      return list(suggested)