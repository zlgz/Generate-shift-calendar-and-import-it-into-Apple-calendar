# -*- coding:utf-8 -*-
# @FileName  :ics_export.py
# @Time      :2024/8/27 17:10
# @Author    :wuzefei
# @WeChat Official Accounts     :扎了个扎
from ics import Calendar, Event
import pandas as pd
from datetime import datetime, timedelta

# User's shift cycle details
cycle = ["白班(住院)", "白班(门诊)", "夜班", "休息"]

# Start date and end date
start_date = datetime(2024, 8, 27)
end_date = datetime(2024, 12, 31)

# Calculate the shifts
current_date = start_date
schedule = []

while current_date <= end_date:
    cycle_day = (current_date - start_date).days % len(cycle)
    schedule.append({'日期': current_date, '班次': cycle[cycle_day]})
    current_date += timedelta(days=1)

# Convert to DataFrame
schedule_df = pd.DataFrame(schedule)

# Create a new calendar
cal = Calendar()

# Populate the calendar with events
for _, row in schedule_df.iterrows():
    event = Event()
    event.name = row['班次']
    event.begin = row['日期'].strftime('%Y-%m-%d')
    event.make_all_day()
    cal.events.add(event)

# Save to an .ics file
with open('work_schedule.ics', 'w') as my_file:
    my_file.writelines(cal)
