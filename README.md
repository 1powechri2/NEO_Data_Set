# ☄️ Near Earth Objects CSV Loader ☄️

--Python Version: 3.5.2

I wrote this so that I could obtain a small but interesting dataset
that could be used to learn data visualization. I know the code is
a little sloppy and repeats itself for the start date and end date
in the date_getter but I don't care. I got my CSV and that's all that
matters.

In order to use it yourself you'll need to get an api key from [NASA](https://api.nasa.gov/api.html#authentication)
and then create an api_key.py file in the neo_getter directory. The api_key.py
file should have 1 line which should be `key = "the api key you got from NASA"`.

This code was designed to only obtain all the near earth objects from 2018 and this
repository has the CSV that was the product of this code's design. If you are wanting
to obtain data from another year and even just a month or a week you'll need to
familiarize yourself with how it works or [email me](https://api.nasa.gov/api.html#authentication).
