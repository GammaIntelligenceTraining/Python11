import pandas as pd
import mysql.connector

pd.set_option('display.max_rows', 160)
pd.set_option('display.max_columns', 9)

df = pd.read_csv('csv_files/2019.csv')

# print(df.groupby('Country or region'))

a = df.nlargest(5, 'Overall rank')
b = df.nsmallest(5, 'Overall rank')

df2 = pd.read_csv('csv_files/test.csv')
# print(a)
# print(b)

print(pd.concat([a, b, df2]))
