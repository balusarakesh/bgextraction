from django.shortcuts import render
from django.http import HttpResponse
from helper import create_temp_directory
from helper import get_random_chars
import os
import cv2
import numpy as np
import boto
from boto.s3.key import Key


def upload_to_s3(location):
    print location
    conn = boto.connect_s3(aws_access_key_id='AKIAI4AR5MAHBVGFMNXQ', aws_secret_access_key='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')
    if os.path.exists(location):
        bucket = conn.get_bucket('bgextraction')
        key = Key(bucket)
        key.key = os.path.basename(location)
        key.set_contents_from_file(open(location, 'rb'))
        key.set_acl('public-read')


def index(request):
    return render(request, 'bgextr/index.html')


def save_file(input_file):
    tmp_dir = create_temp_directory(get_random_chars())
    try:
        input_vid = os.path.join(tmp_dir, 'input_video')
        with open(input_vid, 'wb+') as vid_file:
            for chunk in input_file.chunks():
                vid_file.write(chunk)
        return input_vid
    except:
        print 'error'


def get_bg_image(video_loc, img_loc):
    c = cv2.VideoCapture(video_loc)
    _,f = c.read()
     
    avg2 = np.float32(f)
    
    try: 
        while(1):
            _,f = c.read()
             
            cv2.accumulateWeighted(f,avg2,0.01)
             
            res2 = cv2.convertScaleAbs(avg2)
            cv2.imwrite(img_loc, res2)
            k = cv2.waitKey(20)
         
            if k == 27:
                break
    except:
        pass 


def upload(request):
    location = save_file(request.FILES['uploadedfile'])
    output_dir = os.path.dirname(location)
    img_name = get_random_chars(10) + '.png'
    output_img = os.path.join(output_dir, img_name)
    get_bg_image(location, output_img)
    upload_to_s3(output_img)
    context = {'img_url' :'https://s3-us-west-1.amazonaws.com/bgextraction/' + img_name}
    return render(request, 'bgextr/output.html', context)
