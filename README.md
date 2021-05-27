# Real estate agency website


The site is under construction, so only a page with a list of apartments and an admin panel for filling in the database are available.

## Start

- Download the Code
- Install requirements `pip install -r requirements.txt`
- Crate file database and apply all migrations immediately with the command `python manage.py migrate`
- Start server with command `python manage.py runserver`

## Environments Variables

Some of the project settings are taken from the environment. To define them, create file `.env` with `manage.py` write data format: `ПЕРЕМЕННАЯ=значение`.

Available 3 variables:
- `DEBUG` — debug-mode. 
- `SECRET_KEY` — secret key.
- `ALLOWED_HOSTS` — see [documentation Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — address for database, example: `sqlite:///db.sqlite3`. [documentation](https://github.com/jacobian/dj-database-url)

    This makes it easier to switch between databases.: PostgreSQL, MySQL, SQLite — you need write address.

## Target

The code is written for educational purposes — this is a tutorial in the Python and web development course on the site [Devman](https://dvmn.org/referrals/LKx4rvFOn7SwkzhVrznRuPRs6KUOF6jkJH2oImC2/).
