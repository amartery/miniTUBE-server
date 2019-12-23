# miniTUBE-server
# АРХИТЕКТУРА
корневой URL
http://[hostname]/minitube/api/v1.0/

1) метод HTTP : GET  
URI : http://[hostname]/  
Действие : получить index.html  

2) метод HTTP : GET  
URI : http://[hostname]/minitube/api/v1.0/list_video  
Действие : получить список видео-файлов  

3) метод HTTP : GET  
URI : http://[hostname]/minitube/api/v1.0/list_video/[video_id]  
Действие : получить видео-файл c ID [video_id]  

4) метод HTTP : GET  
URI : http://[hostname]/minitube/api/v1.0/list_video/[video_id]/get_preview  
Действие : получить превью для видео-файла c ID [video_id]  

# DEPENDENCES
nginx  
nginx rtmp-module - https://github.com/arut/nginx-rtmp-module  
pytho3 or python3 with flask  
ffmeg  
dash.js  

# HOW RUN

PYTHON 3  
python3 -m venv myvenv  
source myvenv/bin/activate  
python3 -m  pip install flask  
python3 app.py  

# Для зауска необходим dash.js  
Скачиваем и устанавливаем dash.js из форка  
скачиваем dash.js в /var/www  
cd /var/www  
git clone https://github.com/arut/dash.js.git  
cd dash.js  
git checkout live  
Открываем в редакторе baseline.html и находим строчку со стандартным урлом  
url = "http://dash.edgesuite.net/envivio/dashpr/clear/Manifest.mpd",  
Заменяем на наш урл  
url = "http://localhost:8080/dash/mystream.mpd".  
Далее заходим в браузер на страницу http://localhost:8080/dash.js/baseline.html.  



# CURL
возвращает /home/amartery/tp_progect/templates/index.html  
curl -i http://localhost:5000/  

получение списка доступных видео файлов в дирректории /home/amartery/tp_progect/video  
curl -i http://localhost:5000/minitube/api/v1.0/list_video  

запуск ffmeg для видео с названием <video_id>, возвращает строку http://localhost:8080/dash/mystream<id_thread>.mpd  
curl -i http://localhost:5000/minitube/api/v1.0/list_video/<video_id>  

получене превью
curl -i http://localhost:5000/minitube/api/v1.0/list_video/<video_id>/get_preview


# NGINX
sudo /usr/local/nginx/sbin/nginx -c /home/amartery/tp_progect/d.conf  

ps -ax | grep nginx  
sudo kill -s QUIT 4157  
sudo systemctl stop nginx  


# EXAMPLE
запускаем nginx  
sudo /usr/local/nginx/sbin/nginx -c <your_path>/tp_progect/d.conf  
запуск серевера  
python3 app.py   
получение списка доступных видео файлов в дирректории   <your_path>/video  
curl -i http://localhost:5000/minitube/api/v1.0/list_video  

# FFMEG setup (команда используемая в скрипте python)
ffmpeg -re -i <full_path_to_video> -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://localhost/myapp/mystream
