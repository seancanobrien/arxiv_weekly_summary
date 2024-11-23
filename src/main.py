import datetime

from format import save_as_update_html
from search import search_arxiv
from input import get_filter_vals, get_previous_week_dates, get_mondays_in_range


# input the monday (or tuesday or wednesday,...) of the current week,
# an Arxiv update for the previous week will be made
def make_prev_weekly_update(day, filter_loc, save_dir):
    start_date, end_date = get_previous_week_dates(day)
    authors, keywords, repositories = get_filter_vals(filter_loc)

    # Search arXiv
    matches = search_arxiv(start_date, end_date, authors, keywords, repositories)

    # Save results as HTML
    if matches:
        save_as_update_html(matches, start_date, end_date, authors, keywords, repositories, save_dir + f"{start_date.strftime('%Y-%m-%d')}_weekly_update.html")
    else:
        print("No matching results found.")

# make many weekly updates retrospectively
def make_weekly_updates_in_range(start_date, end_date, filter_loc, save_dir):
    mondays = get_mondays_in_range(start_date, end_date)
    for day in mondays:
        make_prev_weekly_update(day, filter_loc, save_dir)

if __name__ == "__main__":
    filter_file_location = "/home/sean/Documents/arxiv_summary/src/filter.txt"
    save_dir = "/home/sean/Documents/arxiv_weekly_updates/"

    make_weekly_updates_in_range(
        datetime.datetime(2024, 9, 2),
        datetime.datetime(2024, 11, 18),
        filter_file_location,
        save_dir)

    # make_prev_weekly_update(datetime.date.today(), filter_file_location, save_dir)
