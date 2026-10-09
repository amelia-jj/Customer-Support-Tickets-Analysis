import pandas as pd
pd.set_option('display.max_rows', None)

# Load data and check for missing values
df = pd.read_csv('customer_support_tickets.csv')

print(df.shape)
print(df.head())
print(df.isnull().sum())

# Average resolution time
average_resolution = df['resolution_hours'].mean()
print(average_resolution)

# Check how CSAT relates to first response time and resolution time
correlation_response = df['csat_score'].corr(df['first_response_hours'])
correlation_resolution = df['csat_score'].corr(df['resolution_hours'])

print('CSAT vs response time:', correlation_response)
print('CSAT vs resolution time:', correlation_resolution)

# Average CSAT by category, priority and channel
avg_csat_by_category = df.groupby('category')['csat_score'].mean()
print(avg_csat_by_category)

avg_csat_by_priority = df.groupby('priority')['csat_score'].mean()
print(avg_csat_by_priority)

avg_csat_by_channel = df.groupby('channel')['csat_score'].mean()
print(avg_csat_by_channel)

# Average resolution time by priority
avg_resolution_by_priority = df.groupby('priority')['resolution_hours'].mean()
print(avg_resolution_by_priority)

# Sentiment breakdown per category
sentiment_by_category = df.groupby('category')['sentiment'].value_counts()
print(sentiment_by_category)

# Check whether Billing tickets have only Negative sentiment
print(df[df['category'] == 'Billing']['sentiment'].unique())
