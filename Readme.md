Создать образ
- make build
- docker build -t test .

Запустить контейнер
- make run
- docker run -d --rm -p 8000:8000 --name test_work test

Остановить и удалить контейнер
- make stop
- docker stop test_work

localhost:8000/producers/?contract_id=32812

login: root
pass:  root
