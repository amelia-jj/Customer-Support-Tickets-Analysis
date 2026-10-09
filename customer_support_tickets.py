import pandas as pd
pd.set_option('display.max_rows', None)

df = pd.read_csv('customer_support_tickets.csv')

print(df.shape)
print(df.head())
print(df.isnull().sum())

average_resolution = df['resolution_hours'].mean()
print(average_resolution)

correlation_response = df['csat_score'].corr(df['first_response_hours'])
correlation_resolution = df['csat_score'].corr(df['resolution_hours'])

print('CSAT vs response time:', correlation_response)
print('CSAT vs resolution time:', correlation_resolution)

avg_csat_by_category = df.groupby('category')['csat_score'].mean()
print(avg_csat_by_category)

avg_csat_by_priority = df.groupby('priority')['csat_score'].mean()
print(avg_csat_by_priority)

avg_resolution_by_priority = df.groupby('priority')['resolution_hours'].mean()
print(avg_resolution_by_priority)

sentiment_by_category = df.groupby('category')['sentiment'].value_counts()
print(sentiment_by_category)

print(df[df['category'] == 'Billing']['sentiment'].unique())

avg_csat_by_channel = df.groupby('channel')['csat_score'].mean()
print(avg_csat_by_channel)
