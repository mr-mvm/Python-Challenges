def timeConversion(s):
    """
    Converts a 12-hour AM/PM formatted time string to a 24-hour formatted time string.

    Parameters:
        s (str): Time string in 12-hour AM/PM format (e.g., "07:05:45PM").

    Returns:
        str: Time string in 24-hour format (e.g., "19:05:45").
    """
    # Extract the period (AM/PM)
    period = s[-2:]
    # Extract the hour, minutes, and seconds
    hour, minutes, seconds = map(int, s[:-2].split(':'))
    
    if period == 'AM':
        hour = 0 if hour == 12 else hour
    elif period == 'PM':
        hour = hour if hour == 12 else hour + 12

    # Format the time in 24-hour format
    return f"{hour:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter time in 12-hour format (e.g., 07:05:45PM): ")

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
