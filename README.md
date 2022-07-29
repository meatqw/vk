# vk

Терминальное приложения для парсинга пользователей групп и последующего их сохранения в xlsx(табличку)
Приложение работает через vk api по этому для его работы необходим токен доступа.}
Важное примечание (пользователей в группе может быть указано одно кол-во а спарситься может другое, причина - заблокированные пользователи не парсятся)

Как получить этот токен.

1. Авторизовываемся в вк(с любого аккаунта)
2. Создаем приложение(переходим по ссылки) https://vk.com/editapp?act=create
3. В пункте ПЛАТФОРМА выбираем Standalone-приложение
4. Вводим название (ЛЮБОЕ)
5. После создания будет открыта страница приложения елси нет то нудно открыть и из адресной строки скопировать id пложения
 (пример того как выглядит строка https://vk.com/editapp?id=8225378 И ВОТ ТУТ НУЖЕН ТОЛЬКО ID)
6. Генерируем ключ (Заменить YUOR_ID на id приложения и перейти по этой ссылке
https://oauth.vk.com/authorize?client_id=8225378&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.131

7. После этовы вы получите ссылку в адресной строке с ключем
ВОТ ТАКУЮ https://oauth.vk.com/blank.html#access_token=vk1.a.dk1yozyouW1o38lIz5xip0FWqM7IJNZW-yGXccS9VpSQ3pR9yUoqChaHXrisdVO03__jFgPLNbvjQCGLDzvqOa4DgPXrzGfRnOMBr7ZZYgXHm6sa6R3ITPp3DJ0IpX8w0ZQjCKB4gW1W1FY1npYDs_S3wWPR0Wf4EOFHvV5AwN0zcnOWu0RreBcat0U1cyzq-Vr&expires_in=86400&user_id=740976437
Копируем отсюда access_token(весь текст после "access_token=" и до "&expires_in")

И вот этот токен(ЭТО просто пример у вас будет ваш) vk1.a.dk1yozyouW1o38lIz5xip0FWqM7IJNZW24sad-yGXccS9VpSQ3pR9yUoqChaHXrisdVO03__jFgPLNbvjQCGLDzvqOa4DgPXrzGfRnOMBr7ZZYgXHm6s6R3ITPp3DJ0IpX8w0ZQjCKB4gWbFY1npYDs_S3wWPR0Wf4EOFHvV5AwN0zcnOWu0RreB5cat0U1cyzq-Vr
Вставляем без settings.txt после "TOKEN=" без пробелов и знаков
Все, токен получен

SLEEP - это величина сна между запросами, чтобы не словить капчу. Чем больше пользователей в группе, тем больше SLEEP 
Тест проводился на группе в 60000 подписчиков со слипом в 10 сек - КАПЧИ НЕ БЫЛО, но я бы все же рекомендовал ставить слип по более.

КАК ПОЛЬЗОВАТЬСЯ.
Открываем, будет предложено ввести group name/id (название группы - то, что в адрессной строке или id группы), вводим
Ждем
После окончания работы результаты будут записаны в xlsx файл раядом с vkP(v1.0).exe


ФАЙЛ SETTINGS должен лежать рядом с vkP(v1.0).exe иначе программа его не увидет 
Под РЯДОМ емеется ввиду одна директория.
