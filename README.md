🚀 Lightweight News Viewer for Your Terminal! 🚀

The idea of having news headlines appearing on your Terminal without any need of opening a browser or a news app is fascinating. 
It's simple, lightweight and definitely much less distraction. 
This simple yet powerful Python script that brings the latest news headlines directly to your Linux/Mac/Windows terminal! 🖥️✨

This script uses the newsapi library to fetch real-time news and the rich library to beautifully format the output. 
It can display headlines and news articles from categories like Science, Technology, Hollywood, and Sports in a structured, 
easy-to-read format. The auto refreshing feature fetches new set of fresh news articles after every 30 seconds. 

Why I love this script:
Simplicity: No need for heavy browsers or apps. Just run the script and get your news!
Lightweight: Minimal resource usage, perfect for any Linux system.
Real-Time Updates: Fetches fresh news every 30 seconds, ensuring you never miss out on the latest happenings.
Customizable: Easily tweak the categories and display settings to suit your preferences.
Technical Highlights:
NewsAPI Integration: Uses newsapi to fetch top headlines and category-specific news articles.
Rich Formatting: Utilizes the rich library to create a visually appealing layout with 3 columns and 2 rows, filling the entire terminal screen.
Dynamic Layout: The first column merges cells from both rows for headlines, while the second and third columns display category-specific news.
Auto-Refresh: The terminal screen refreshes every 30 seconds, fetching the latest news from the past 48 hours.
