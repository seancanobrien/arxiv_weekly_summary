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
                authors.append(line)
            elif current_section == "keywords":
                keywords.append(line)
            elif current_section == "repositories":
                repositories.append(line)

    return authors, keywords, repositories

def get_previous_week_dates(date):

    today = date

    # Calculate the difference between today and the most recent Monday
    days_since_monday = today.weekday()

    # Monday of the current week
    monday_this_week = today - datetime.timedelta(days=days_since_monday)

    # Monday of the previous week
    monday_previous_week = monday_this_week - datetime.timedelta(weeks=1)

    # Sunday of the previous week (6 days after the previous Monday
    sunday_previous_week = monday_previous_week + datetime.timedelta(days=6)

    return monday_previous_week, sunday_previous_week

def get_mondays_in_range(start_date, end_date):
    mondays = []

    # Adjust start_date to the first Monday after or on the start_date
    days_to_monday = (7 - start_date.weekday()) % 7
    first_monday = start_date + datetime.timedelta(days=days_to_monday)

    # Loop through dates from first_monday to end_date, with a step of 7 days
    current_monday = first_monday
    while current_monday <= end_date:
        mondays.append(current_monday)
        current_monday += datetime.timedelta(weeks=1)

    return mondays
