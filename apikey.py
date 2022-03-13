import datetime
current_time = datetime.datetime.now(datetime.timezone.utc)
current_time = current_time.timestamp() # works if Python >= 3.3

new_end_date = current_time + (43800*3* 60)  # 5 min * 60 seconds
print (new_end_date)