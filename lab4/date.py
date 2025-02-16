from datetime import datetime, timedelta

#Write a Python program to subtract five days from current date.
current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime('%Y-%m-%d'))
print("Date Five Days Ago:", new_date.strftime('%Y-%m-%d'))


#Write a Python program to print yesterday, today, tomorrow.
today = datetime.now().date()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


#Write a Python program to drop microseconds from datetime.
now_with_microseconds = datetime.now()

now_without_microseconds = now_with_microseconds.replace(microsecond=0)

print("With Microseconds:", now_with_microseconds)
print("Without Microseconds:", now_without_microseconds)


#Write a Python program to calculate two date difference in seconds.
date1 = datetime(2025, 2, 17, 12, 0, 0)
date2 = datetime(2025, 2, 18, 14, 30, 0)

time_difference = date2 - date1

difference_in_seconds = time_difference.total_seconds()

print("Difference in Seconds:", difference_in_seconds)
