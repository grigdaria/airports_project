Базу данных реализовать на сервисе supabase.com
Файлы для импорта
- coastline (контуры береговой линии, списки точек с широтой и долготой)
- icao (данные по рейсам, имя файла это icao борта)
- airports (данные по местоположени аэропортов)
- stations (координаты приемников сигналов маячков самолетов, в файлах рейсов за
приемник отвечает поле src, если None - то это приемник 1)
Написать функции на plpgsql для реализации api, протестировать функции на сервисе
postman.com
На сервисе pythonanywhere.com реализовать приложение на python+flask, отображающее
карту мира и аэропорты. при выборе аэропорта отобразить увеличенный фрагмент карты
с возможностью отображения на этом фрагменте в указанный момент времени всех
самолетов. Взаимодействие с базой осуществлять только через реализованные функции
api.
По итогам предоставить git репозиторий с исходными текстами приложения и скриптами
импорта данных, добавив ссылки на postman и pythonanywhere, на сайте dbdiargam.io
создать схему базы данных и опубликовать документацию к базе на dbdocs.io, ссылки на
оба ресурса приложить к репозиторию.

1. БД реализована на сервисе supabase.com
2. Импортированы все файлы в качестве данных для таблиц
3. Написаны функции get_shapes(), get_flights(), get_all_coastline(), get_all_airports(), get_airport_by_name(name), get_airport_by_id(id)
4. На сервисе postman.com протестирована каждая функция:
   Пример запросов 
    https://gzvczizfaitegduuldza.supabase.co/rest/v1/rpc/get_airport_by_id
   с указанными параметрами (SUPABASE_API_KEY, SUPABASE_URL)
6. На сервисе pythonanywhere.com реализован проект на python+flask, отображающий карту мира и аэропорты, при выборе аэропорта отображается увеличенный фрагмент карты, с возможностью ввода даты, для отображения в указанный момент времени всех самолетов (реализовано не до конца)
7. Взаимодействие с БД осуществляется благодаря функция в БД.


   
