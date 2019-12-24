import pandas as pd

data_one = pd.read_csv('data_a.csv')
data_two = pd.read_csv('data_p.csv')
print('Data loaded')

data_one = data_one.drop(['id'], axis=1)
data_one = data_one.rename(columns={'Date': 'date','Installs': 'installs','Campaign':'campaign'})
data_one.installs = data_one.installs.astype(int)
data_two = data_two.drop(['campaign'], axis=1)
print('Drop unwanted data & fix names')

lol = pd.merge(data_one, data_two, on=['ad_id','date'], how='left').\
        drop(['ad_id'], axis=1).\
        groupby(['date','campaign','os','app']).\
        sum().\
        sort_values(['campaign','app','os','date']).\
        reset_index().\
        reindex(columns=['app','date','campaign','os','installs','spend','cpi'])
df = lol[lol.installs != 0].copy()
df['cpi'] = df['spend']/df['installs']
dr = df.round({'spend': 2, 'cpi': 2})
print('Done processing')
dr.to_csv('out.csv',index=False)
print('Output file created')
quit()