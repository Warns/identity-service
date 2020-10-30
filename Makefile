build:
	docker-compose build
up:
	docker-compose up -d
run:
	docker-compose stop web && docker-compose run -p 8000:8000 -v $(shell pwd):/app web
restart:
	docker-compose restart
stop:
	docker-compose stop
destroy:
	docker-compose down
ps:
	docker-compose ps
api-logs:
	docker-compose logs  --tail 10 --follow web
shell:
	docker-compose exec web /bin/sh
django-shell:
	docker-compose exec web python manage.py shell
psql:
	docker-compose exec postgres psql -U postgres postgres
migrate:
	docker-compose exec web python manage.py migrate
makemigrations:
	docker-compose exec web python manage.py makemigrations
test:
	docker-compose exec web python manage.py test