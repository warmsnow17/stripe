## Django + stripe

В приложении используется докер.

Выполните следующие команды:

1. docker-compose up -d --build
2. docker-compose exec web python manage.py makemigrations 
3. docker-compose exec web python manage.py migrate
4. docker-compose exec web python manage.py createsuperuser
5. создайте админа -> зайдите в админ панель по адресу: http://0.0.0.0:8000/admin/ -> создайте товар (из stripe будет подтянут товар T-shirt)
6. перейдите по адресу: http://0.0.0.0:8000/item/1/ -> нажмите buy
7. в форме оплаты введите адрес эл.почты, номер карты 4242 4242 4242 4242, любой месяц/год, любой cvv -> нажмите оплатить
8. после удачной оплаты вы увидите страницу с текстом 'Thanks for your order!!!!'

