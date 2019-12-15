# miniTUBE-server
# АРХИТЕКТУРА

корневой URL
http://[hostname]/minitube/api/v1.0/

1) метод HTTP : GET  
URI : http://[hostname]/minitube/api/v1.0/list_video  
Действие : получить список видео-файлов  

2) метод HTTP : GET  
URI : http://[hostname]/minitube/api/v1.0/list_video/[video_id]  
Действие : получить видео-файл c названием [video_id]  

3) метод HTTP : GET  
URI : http://[hostname]/  
Действие : получить index.html  


# HOW RUN

PYTHON 3  
python3 -m venv myvenv  
source myvenv/bin/activate  
python3 -m  pip install flask   
python3 app.py  

PYTHON 2  
virtualenv flask  
flask/bin/pip install flask  
chmod a+x app.py  
./app.py  


Для зауска необходим dash.js  
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

запуск ffmeg для видео с названием <video_id>  
curl -i http://localhost:5000/minitube/api/v1.0/list_video/<video_id>  



# NGINX
sudo /usr/local/nginx/sbin/nginx -c /home/amartery/tp_progect/d.conf  

ps -ax | grep nginx  
sudo kill -s QUIT 4157  
sudo systemctl stop nginx  


# EXAMPLE
запускаем nginx  
sudo /usr/local/nginx/sbin/nginx -c <your_path>/tp_progect/d.conf  
запуск серевера  
chmod a+x app.py  
./app.py  
получение списка доступных видео файлов в дирректории   <your_path>/video  
curl -i http://localhost:5000/minitube/api/v1.0/list_video  

# FFMEG setup (команда используемая в скрипте python)
ffmpeg -re -i <full_path> -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://localhost/myapp/mystream
