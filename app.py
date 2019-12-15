#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
from collections import deque

import os
import uuid
import subprocess as sp



app = Flask(__name__)


# def create_list_video():
#     # get list available video files in /home/amartery/tp_progect/video
#     directory = '/home/amartery/tp_progect/video'  # add the path to the folder with the video files
#     files = os.listdir(directory)
#     filtered_files = filter(lambda x: x.endswith('.mp4'), files)  # only mp4 files

#     files_queue = deque()
#     files_queue += filtered_files

#     list_video = []
#     while files_queue:
#         id_num = str(uuid.uuid4())  # generate random sequence with uuid
#         video = {
#             'id': id_num[1:5],  # assigning a unique ID with a length of 4
#             'title': files_queue.popleft()
#         }
#         list_video.append(video)
#     return list_video



def create_list_video():
    # get list of   available video files in /home/amartery/tp_progect/video
    directory = '/home/amartery/tp_progect/video'  # add the path to the folder with the video files
    files = os.listdir(directory)
    filtered_files = filter(lambda x: x.endswith('.mp4'), files)  # only mp4 files

    files_queue = deque()
    files_queue += filtered_files

    list_video = {}
    while files_queue:
        id_num = str(uuid.uuid4())  # generate random sequence with uuid
        list_video.update({id_num[1:5]: files_queue.popleft()})
    return list_video



list_video = create_list_video()  #creating list of available video files


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)
 
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)



@app.route('/')
def index():
    """miniTube home page."""
    return render_template('index.html')


@app.route('/minitube/api/v1.0/list_video', methods=['GET'])
def get_list_video():
    return jsonify({'available video files': list_video})


@app.route('/minitube/api/v1.0/list_video/<string:video_id>', methods=['GET'])
def get_video(video_id):
    if video_id not in list_video.keys():
        abort(404)

    filename = list_video[video_id]
    full_path = '/home/amartery/tp_progect/video/' + filename
    command = 'ffmpeg -re -i {} -vcodec libx264 -vprofile baseline -g 30 -acodec aac -strict -2 -f flv rtmp://localhost/myapp/mystream'.format(full_path)
    sp.call(command,shell=True)
    return "ffmpeg started\n"



if __name__ == '__main__':
    app.run(debug=True)
