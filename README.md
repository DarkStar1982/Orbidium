# Orbidium

An app demo showing asteroid orbits using NASA MPC database.

Features basic 2D rendering as well as parsing of MPC datafile

![all asteroids](https://raw.githubusercontent.com/DarkStar1982/Orbidium/refs/heads/main/doc/Screenshot%205.png?raw=true)

Join our Discord community for more cool space stuff: https://discord.gg/4WNY6yVVk6

## TODO
- Add ephemeris data to show actual position of the asteroid on its orbit with respect to current time.
- Add 3D view using WebGL.

## Development

The project is in "works on my Macbook" state of maturity, report any bugs on Github, or better fork and modify on your own.

### Local

- To run and test
  - Install dependencies using `pip install -r requirements.txt`
  - run migrations using `python manage.py migrate` command
  - populate the local db using `python manage.py process_mpc_file` command
  - run locally via `python manage.py runserver 0.0.0.0:8000`
-

### Docker

- Start the server with `docker compose up -d`
- Populate the database with `docker compose exec app make setup`
  (this may take some time)
- Open your browser to `localhost:8000`

> If you modify the dependencies (requirements.txt), you'll want to rebuild the image with `docker compose up --build -d`
