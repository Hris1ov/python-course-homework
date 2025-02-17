# Constants
astronomical_hour_in_minutes = 60  # 1 astronomical hour = 60 minutes
academical_hour_in_minutes = 40    # 1 academical hour = 40 minutes
break_duration_in_minutes = 20     # 20-minute break per session

# Get user input
total_academical_hours = 64

# Total time for the course (in minutes), including breaks
total_course_time_in_minutes = (total_academical_hours * academical_hour_in_minutes) + (total_academical_hours // 4 * break_duration_in_minutes)

# Convert the total course time to astronomical hours
total_course_time_in_astronomical_hours = total_course_time_in_minutes / astronomical_hour_in_minutes

# Output the result
print(f"Total course duration in astronomical hours: {total_course_time_in_astronomical_hours:.2f}")
