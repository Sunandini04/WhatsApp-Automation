# WhatsApp Automation

This project allows a user to send scheduled text messages using the Textbelt API. A user can easily set up this script to send messages at specified intervals or at a specific time every day.

## Features

- Schedule text messages to be sent at regular intervals.
- Customize the message and recipient phone number.
- Easy to set up and run.

## Requirements

- Python 3.x
- `requests` library
- `schedule` library

## Setup

1. **Install the required libraries:**
    ```bash
    pip install requests schedule
    ```

2. **Create a `credentials.py` file in the project directory and add your mobile number:**
    ```python
    # credentials.py
    mobile_number = 'your_mobile_number'
    ```

3. **Run the script:**
    ```bash
    python scheduler.py
    ```

## Usage

- The script will send a text message every 10 seconds by default.
- To change the schedule, modify the `schedule.every(10).seconds.do(send_text)` line in `scheduler.py` to your desired schedule.
- To send a message at a specific time every day, uncomment the line:
    ```python
    # schedule.every().day.at('10:00').do(send_text)
    ```

