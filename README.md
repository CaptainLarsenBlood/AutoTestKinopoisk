# AutoTestKinopoisk
Автотесты для проверки фильтрации на сайте кинопоиска в разделе топ 250

В pages описана страница через PO
В elements описаны базовые элементы и фильтры через EO
В conftest описаны фикстуры. Чтобы каждый раз не прокидывать фикстуру драйвера в тесты, она прокидывается сразу в класс и поэтому доступна из тестов.

Что можно доработать:
1) Сейчас эталоны парсятся вручную через get_films(), можно добавить парсинг через request.get и bs4, но тогда надо подумать как не попадать на капчу при подобных запросах. Можно добавить обновление эталонов просто после падения теста на этапе сравнения.
2) Доработать setup_class чтобы PO объявлялось только один раз,а не перед каждым вызовом теста в setup()
