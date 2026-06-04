import pandas as pd 


train = pd.read_csv('train.csv',usecols=['Survived'])
a,b = train['Survived'].value_counts(normalize=True)
print('Умерло',round(a,2)*100,'процентов')
print('Выжило',round(b,2)*100,'процентов')
