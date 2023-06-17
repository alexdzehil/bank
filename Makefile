build:
	docker build -t test .

run:
	docker run -d --rm -p 8000:8000 --name test_work test

stop:
	docker stop test_work
