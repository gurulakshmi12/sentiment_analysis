# Sentiment Analysis System

## Overview

The Sentiment Analysis System is a web-based application built using Django that analyzes the sentiment of user-provided text. It utilizes Hugging Face Transformers for natural language processing and sentiment analysis. The project includes a front end built with HTML and CSS, and uses a local database for data storage.

## Features

- User-friendly interface for sentiment analysis
- Displays sentiment results (positive, negative, neutral)
- Responsive design

## Technologies Used

- **Backend**: Django, Python, Hugging Face Transformers
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (local database)

## Installation

### Prerequisites

- Python 3.x
- Django
- Hugging Face Transformers

### Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**
    ```sh
    python manage.py runserver
    ```

6. **Open your browser**
    Navigate to `http://127.0.0.1:8000` to see the application in action.

## Project Structure


