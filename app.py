#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template, send_file
from collections import deque
from flask_cors import CORS, cross_origin

import os
import uuid
import subprocess as sp
import time
import os.path





app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def create_list_video():  # available video files in /home/amartery/tp_progect/video
    directory = '/home/amartery/aksdfhk/video'  # add  the <yor_path_to_video>/video/
    files = os.listdir(directory)
    filtered_files = filter(lambda x: x.endswith('.mpd'), files)  # only mp4 files

    files_queue = deque()  # create a queue of files
    files_queue += filtered_files

    list_video = {}
    while files_queue:
        id_num = str(uuid.uuid4())  # generate random sequence with uuid
        """  
        the next line adds a new key-value pair to the dictionary, 
        where the key is unique ID with a length of 4
        the value is the file name from the queue
        """
        list_video.update({id_num[1:5]: files_queue.popleft()})
    return list_video


list_video = create_list_video()  #creating list of available video files


@app.errorhandler(400)   # 400 error detecting
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 

@app.errorhandler(404)   # 404 error detecting
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/')  # miniTube home page
def index():
    return render_template('index.html')


@app.route('/minitube/api/v1.0/list_video', methods=['GET'])  # available video page
@cross_origin()
def get_list_video():
    return jsonify({'available video files': list_video})


 

@app.route('/minitube/api/v1.0/list_video/<string:video_id>', methods=['GET'])
@cross_origin()
def get_video(video_id):

    if video_id not in list_video.keys():
        abort(404)

    filename = list_video[video_id]
    full_path = '/home/amartery/aksdfhk/video/' + filename  # add  the <yor_path_to_video>/video/
    return 'http://localhost:8080/video/{}'.format(filename)


@app.route('/minitube/api/v1.0/list_video/<string:video_id>/get_preview')
def get_preview(video_id):
    if video_id not in list_video.keys():
        abort(404)

    name_video_file = list_video[video_id]
    name = name_video_file[:-3]  # remove the file extension (mp4)
    filename = name + 'jpg'  # add new extension (jpg)
    full_path = '/home/amartery/aksdfhk/preview/' + filename  # add  the <yor_path_to_preview>/preview/
    return send_file(full_path, mimetype='image/gif')




if __name__ == '__main__':
    app.run(debug=True)
