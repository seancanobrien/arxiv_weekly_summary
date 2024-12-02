import datetime

def get_filter_vals(filename):
    authors = []
    keywords = []
    repositories = []
    current_section = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            # Skip empty lines or comment lines
            if not line or line.startswith("#"):
                continue

            # Detect section headings
            if line == "AUTHORS:":
                current_section = "authors"
                continue
            elif line == "KEYWORDS:":
                current_section = "keywords"
                continue
            elif line == "REPOSITORIES:":
                current_section = "repositories"
                continue

            # Add content to the appropriate section
            if current_section == "authors":
                authors.append(line.strip())
            elif current_section == "keywords":
                keywords.append(line.strip())
            elif current_section == "repositories":
                repositories.append(line.strip())

    return authors, keywords, repositories

def get_previous_week_dates(date):
    # Calculate the difference between today and the most recent Monday
    days_since_monday = date.weekday()
    # Monday of the current week
    monday_this_week = date - datetime.timedelta(days=days_since_monday)
    # Monday of the previous week
    monday_previous_week = monday_this_week - datetime.timedelta(weeks=1)
    # Sunday of the previous week (6 days after the previous Monday
    sunday_previous_week = monday_previous_week + datetime.timedelta(days=6)

    return monday_previous_week, sunday_previous_week

def mondays_starting_week_in_range(start_date, end_date):
    """
    Returns a list of Mondays that start a week within the given date range.

    Parameters:
        start_date (datetime): The starting date of the range.
        end_date (datetime): The ending date of the range.

    Returns:
        list[datetime]: A list of Mondays marking the start of a week in the range.
    """
    # Normalize start_date to the previous Monday if it's not already a Monday
    start_date += datetime.timedelta(days=-start_date.weekday())

    # Generate Mondays within the range
    mondays = []
    while start_date <= end_date:
        mondays.append(start_date)
        start_date += datetime.timedelta(weeks=1)

    return mondays
