#!/env/bin/python

# - [ ] column two unicode validation (with commas)
# - [ ] column 7 replace invalid UTF-8 characters with the unicode replacement character

import pandas as pd
import pytz
import sys

# import sample file
#df = pd.read_csv('sample.csv')
df = pd.read_csv(sys.stdin)

# convert timestamp column to US/Eastern time zone
#df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
df.index = pd.to_datetime(df.index)
df.index = df.index.tz_localize('US/Pacific')
df.index = df.index.tz_convert('America/New_York')


# convert zip column to be five digits (zero padded prefix)
df['ZIP'] = df['ZIP'].apply(lambda x: '{0:0>5}'.format(x))

# make column FullNameuppercase
df['FullName'] = df['FullName'].str.strip().str.upper()

# convert FooDuration and BarDuration to floating point
df['FooDuration']= pd.to_timedelta(df['FooDuration']).dt.total_seconds()
df['BarDuration']= pd.to_timedelta(df['BarDuration']).dt.total_seconds()

# sum columns FooDuration and BarDuration for column TotalDuration
df['TotalDuration'] = df['FooDuration'] + df['BarDuration']

# export file
df.to_csv('test.csv', encoding='utf-8')
