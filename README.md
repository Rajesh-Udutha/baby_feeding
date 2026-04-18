Baby Feeding

The Baby Feeding application allows user to log the feeding time for the baby on time basis.

It is an open-source tool that reads the data from the user and represents data in metrics. 

Remindes the feeding time by sending notification  for the baby by analyzing the existing data. Allows user to export the data as well.

Quick Start

Prerequisites

    Python 3.10+

Installation

    # Clone the repo

    git clone https://github.com/Rajesh-Udutha/baby_feeding.git

    cd baby_feeding

    #install dependencies
    pip install -r requirements.txt


    #run the migrations
    flask db init
    flask db migrate -m "initial tables"
    flask db upgrade

    #run the app
    python app.py

open http://127.0.0.1:8000/ in the browser


Project Structure

    baby_feeding/
    ├── app.py                 # Main Flask app
    ├── requirements.txt       # Python dependencies
    ├── .gitignore
    ├── README.md
    ├── config.py              # Configuration
    ├── models/
    │   └── user.py
    │   └── baby.py
    │   └── feeding.py
    ├── routes/
    │   └── auth.py
    │   └── babies.py
    │   └── feedings.py
    ├── tests/
    │   └── test_auth.py
    └── venv/                  # Virtual environment

License
    Use it however you want

Acknowledgment

    Built with
        Flask   - Framework
        FastAPI - Web Server
        