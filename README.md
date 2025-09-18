# Coders-of-Delhi
# Social Network Data Processor

This repository contains Python scripts to manage and analyze social network data. It provides tools to clean raw data, display user connections, and generate friend and page recommendations.

## Features

- **Data Cleaning:** Removes users with missing names, duplicate friends, inactive users (no friends or liked pages), and duplicate pages.
- **Display Data:** Shows users, their friends, and liked pages.
- **Friend Recommendations:** Suggests people a user may know based on mutual friends.
- **Page Recommendations:** Suggests pages a user may like based on shared interests.

## Files

- `clean_data.py`: Cleans raw social network data and saves cleaned data.
- `clened_data_display.py` & `read_display.py`: Load and display user and page data.
- `people_you_may_know.py`: Generates friend recommendations for a given user.
- `pages_you_may_like.py`: Generates page recommendations for a given user.
- `incomplete_data.json`: Raw input data with inconsistencies.
- `cleaned_data.json`: Cleaned and processed data.
- `massive_data.json`: Large dataset used for recommendations.

## Usage

1. Clean the raw data:

2. Display the cleaned data connections:

3. Get friend recommendations:

4. Get page recommendations:

## Requirements

- Python 3.x
- JSON module (standard with Python)
