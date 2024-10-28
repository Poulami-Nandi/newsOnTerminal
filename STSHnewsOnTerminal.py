import os
import time
from newsapi import NewsApiClient
from rich.console import Console
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
import shutil
import datetime

# Initialize the NewsApiClient with API key
newsapi = NewsApiClient(api_key='API_KEY')

# Function to get the terminal size
def get_terminal_size():
    columns, rows = shutil.get_terminal_size()
    return rows, columns

# Function to process news heading
def process_news_heading(heading_list):
    return [h.split(" - ")[0] for h in heading_list]

# Function to fetch headlines
def fetch_headlines():
    headlines = newsapi.get_top_headlines(language='en', page_size=10)
    return process_news_heading(["- " + article['title'] for article in headlines['articles']])

# Function to fetch news by category
def fetch_news_by_category(category, start_date, end_date):
    news = newsapi.get_everything(q=category, language='en', from_param='2024-10-26', to='2024-10-28', page_size=10)
    return process_news_heading( ["- " + article['title'] for article in news['articles']])

# Function to create the layout
def create_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
    )
    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="center", ratio=2),
        Layout(name="right", ratio=2),
    )
    layout["right"].split_column(
        Layout(name="top_right", ratio=1),
        Layout(name="bottom_right", ratio=1),
    )
    layout["center"].split_column(
        Layout(name="top_center", ratio=1),
        Layout(name="bottom_center", ratio=1),
    )
    return layout

# Function to update the layout with news
def update_layout(layout):
    headlines = fetch_headlines()
    to_date = datetime.date.today()
    from_date = to_date - datetime.timedelta(days=2)
    science_news = fetch_news_by_category('science', from_date, to_date)
    tech_news = fetch_news_by_category('technology', from_date, to_date)
    hollywood_news = fetch_news_by_category('hollywood', from_date, to_date)
    sports_news = fetch_news_by_category('sports', from_date, to_date)

    layout["left"].update(Panel("\n".join(headlines), title="Headlines"))
    layout["top_center"].update(Panel("\n".join(science_news), title="Science"))
    layout["bottom_center"].update(Panel("\n".join(tech_news), title="Technology"))
    layout["top_right"].update(Panel("\n".join(hollywood_news), title="Hollywood"))
    layout["bottom_right"].update(Panel("\n".join(sports_news), title="Sports"))

# Main function to run the application
def main():
    console = Console()
    layout = create_layout()

    while True:
        update_layout(layout)
        console.clear()
        console.print(layout)
        time.sleep(30)

if __name__ == "__main__":
    main()
