import pandas as pd 


#initialize variables
yo = pd.read_excel('fof2.xlsx')
yo.to_csv('fof2.csv', index=False)
