# Date and time variables
init python:
    current_segment_index = 0
    current_day_index = 0
    current_month_index = 8
    current_year = 2024
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    # Create a list for 15-minute segments starting at 9 AM to 1 AM
    day_segments = [
        "9:00 AM", "9:15 AM", "9:30 AM", "9:45 AM", "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM",
        "11:00 AM", "11:15 AM", "11:30 AM", "11:45 AM", "12:00 PM", "12:15 PM", "12:30 PM", "12:45 PM",
        "1:00 PM", "1:15 PM", "1:30 PM", "1:45 PM", "2:00 PM", "2:15 PM", "2:30 PM", "2:45 PM",
        "3:00 PM", "3:15 PM", "3:30 PM", "3:45 PM", "4:00 PM", "4:15 PM", "4:30 PM", "4:45 PM",
        "5:00 PM", "5:15 PM", "5:30 PM", "5:45 PM", "6:00 PM", "6:15 PM", "6:30 PM", "6:45 PM",
        "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM", "8:00 PM", "8:15 PM", "8:30 PM", "8:45 PM",
        "9:00 PM", "9:15 PM", "9:30 PM", "9:45 PM", "10:00 PM", "10:15 PM", "10:30 PM", "10:45 PM",
        "11:00 PM", "11:15 PM", "11:30 PM", "11:45 PM", "12:00 AM", "12:15 AM", "12:30 AM", "12:45 AM",
        "1:00 AM"
    ]

# Function to get current date and time as a string
init python:
    def get_current_date_time():
        segment = day_segments[current_segment_index % len(day_segments)]
        day = days_of_week[current_day_index % len(days_of_week)]
        month = months[current_month_index % len(months)]
        day_value = (current_day_index % 30) + 1  # Assuming 30 days in a month for simplicity
        return "{}, {} {}, {} - Time: {}".format(day, month, day_value, current_year, segment)


    def get_segment():
        section = day_sections[current_section_index % len(day_sections)]
        return section


# Function to advance time
init python:
    def advance_time(num_segments):
        global current_segment_index, current_day_index, current_month_index, current_year
        global hazel_current_capacity, hazel_digestion_rate
        global reb_current_capacity, reb_digestion_rate
        global sophia_current_capacity, sophia_digestion_rate

        # Calculate the new segment index
        new_segment_index = current_segment_index + num_segments
        
        # Check if we are crossing one or more days
        if new_segment_index >= len(day_segments):
            # Calculate the number of days passed
            days_passed = new_segment_index // len(day_segments)
            
            # Update the current_segment_index to the correct position within the new day
            current_segment_index = new_segment_index % len(day_segments)
            
            # Advance the day index by the number of days passed
            current_day_index += days_passed

            # Handle month and year changes if necessary
            if current_day_index >= 30:  # assuming 30 days in a month for simplicity
                current_day_index %= 30
                current_month_index += 1

                if current_month_index >= len(months):
                    current_month_index = 0
                    current_year += 1

            # If we crossed a day boundary, call end_day
            renpy.jump("end_day")

        else:
            # If not crossing a day boundary, simply update the segment index
            current_segment_index = new_segment_index

# Screen to display date and time
screen date_time_display:
    frame:
        at top
        vbox:
            text get_current_date_time() size 25