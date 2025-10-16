import re

def main():
    print(convert(input("Hours: ")))

# def convert(s):
#     try:
#         start, end = s.split(" to ")
#         if ":" in start:
#             hour1, minute1 = start.split(":")
#             min1 = minute1[0:2]
#         if ":" not in start:
#             hour1 = (start.split(" "))[0]
#             min1 = '00'
#         if ":" in end:
#             hour2, minute2 = start.split(":")
#             min2 = minute2[0:2]
#         if ":" not in end:
#             hour2 = (start.split(" "))[0]
#             min2 = '00' 
#         if ((int(hour1) < 12) and (minute1.endswith("PM"))):
#             hour1 = int(hour1) + 12
#         if ((int(hour2) < 12) and ("PM" in minute2)):
#             hour2 = int(hour2) + 12
#         return f"{hour1}:{min1} to {hour2}:{min2}"
#     except Exception:
#         raise ValueError
    

    # The code below improves the convert function to handle all specified input formats and output in 24-hour format.

    # Update parse_time to check for valid minutes
def parse_time(time_str):
    match = re.match(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)", time_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError
    hour = int(match.group(1))
    minute = int(match.group(2)) if match.group(2) else 0
    if minute >= 60:
        raise ValueError
    period = match.group(3).upper()
    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"
# def parse_time(time_str):
#     match = re.match(r"(\d{1,2})(?::(\d{2}))?\s*(AM|PM)", time_str.strip(), re.IGNORECASE)
#     if not match:
#         raise ValueError
#     hour = int(match.group(1))
#     minute = int(match.group(2)) if match.group(2) else 0
#     period = match.group(3).upper()
#     if period == "PM" and hour != 12:
#         hour += 12
#     if period == "AM" and hour == 12:
#         hour = 0
#     return f"{hour:02}:{minute:02}"

def convert(s):
    try:
        start, end = s.split(" to ")
        start_24 = parse_time(start)
        end_24 = parse_time(end)
        return f"{start_24} to {end_24}"
    except Exception:
        raise ValueError
    

main()