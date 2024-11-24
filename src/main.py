import sys
import os
import datetime

from format import save_as_update_html
from search import search_arxiv
from input import get_filter_vals, get_previous_week_dates, mondays_starting_week_in_range


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
    mondays = mondays_starting_week_in_range(start_date, end_date)
    for day in mondays:
        make_prev_weekly_update(day, filter_loc, save_dir)

if __name__ == "__main__":

    start_date = sys.argv[1]
    end_date = sys.argv[2]
    filter_file_location = sys.argv[3]
    save_dir = sys.argv[4]
    

    if start_date == "t":
        resolved_start_date = datetime.datetime.today()
    else:
        resolved_start_date = datetime.datetime.strptime(start_date, "%Y-%m-$d")

    if end_date == "t":
        resolved_end_date = datetime.datetime.today()
    else:
        resolved_end_date = datetime.datetime.strptime(end_date, "%Y-%m-$d")

    resolved_filter_file_location = os.path.abspath(filter_file_location)

    if save_dir == ".":
        resolved_save_dir = os.getcwd() + "/"
    else:
        resolved_save_dir = os.path.abspath(save_dir) + "/"

    make_weekly_updates_in_range(
        resolved_start_date,
        resolved_end_date,
        resolved_filter_file_location,
        resolved_save_dir)
