# BairesDev Time Tracker

Yes, my friend, now you can track your working hours from the terminal!

## How to install

Clone the repo and go `pip install -r requirements.txt`.

Make sure you've got the last chromedriver from https://chromedriver.chromium.org.

Also, you need to add your credentials to the `lib/config.py` file.

## How to use
You can track time like this

`python main.py --description "I was doing stuff" --hours 4 --date "dd/mm/YYYY"`

Then it'll track you were doing stuff for 4 hours on day `dd` of the month `mm`