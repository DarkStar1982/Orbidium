clean:
	rm ./data/db.sqlite3
	rm MPCORB.DAT

migrate:
	python manage.py migrate

seed:
	python manage.py process_mpc_file

setup: migrate seed

serve:
	python manage.py runserver 0.0.0.0:8000

shell:
	docker compose exec -it app bash