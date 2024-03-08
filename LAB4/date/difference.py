import datetime
date1 = datetime.datetime(2024, 2, 16, 12, 0, 0) 
date2 = datetime.datetime(2024, 2, 15, 12, 0, 0)  
date_difference = date1 - date2
difference_in_seconds = date_difference.total_seconds()
print("Difference between the two dates in seconds:", difference_in_seconds)