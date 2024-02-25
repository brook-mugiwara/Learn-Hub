from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
# from .models import Question, Choice
import pandas as pd
import ast
import google.generativeai as genai
import markdown2
from bs4 import BeautifulSoup
import re



# Create your views here.
def home_page(request):
    return render(request,'./index.html')

def player_page(request,id):

    new_video_key = request.GET.get('new_video_key')
    
    df              = pd.read_csv(r'LearnHub\data\video_list.csv')
    new_df          = df[df['playlist_id'] == id]

    video_str       = new_df['video_list'].values[0]
    video_list      = ast.literal_eval(video_str)

    video_name      = video_list[0]['title']

    if new_video_key:
        video_key = new_video_key
        for x in video_list:
            if x['video_id'] == new_video_key:
                video_name = x['title']
                break
    else:
        video_key = video_list[0]['video_id']


    variable_dict   = {
        'playlist_id': id,
        'video_name' : video_name,
        'dict_list'  : video_list,
        'video_key'  : video_key
    }
    
    return render(request,'./player.html',variable_dict)

def course_page(request):
    # df = pd.read_csv(r'data\video_data.csv')
    df = pd.read_csv(r'LearnHub\data\playlist_data.csv')
    unit_list = list(df['Unit'].unique())
    text_dict = {}
    counter   = 1
    position  = 1
    course_list= ['Kinematics','Electrostatics','Thermodynamics','Gravitation','Kinetic Theory of Gases']

    for x in course_list:
        df_new = df[(df['Unit'] == x)&(df['Rank']<4)]

        text_dict[f'title{position}'] = x

        text_dict[f'title{position}_text{counter}']   = df_new[df_new['Rank'] == 1]['Title'].values[0]
        text_dict[f'title{position}_text{counter+1}'] = df_new[df_new['Rank'] == 2]['Title'].values[0]
        text_dict[f'title{position}_text{counter+2}'] = df_new[df_new['Rank'] == 3]['Title'].values[0]

        text_dict[f'title{position}_plid{counter}']   = df_new[df_new['Rank'] == 1]['Playlist ID'].values[0]
        text_dict[f'title{position}_plid{counter+1}'] = df_new[df_new['Rank'] == 2]['Playlist ID'].values[0]
        text_dict[f'title{position}_plid{counter+2}'] = df_new[df_new['Rank'] == 3]['Playlist ID'].values[0]

        position += 1


    return render(request, './courses.html',text_dict)


def change_video(request):
    new_video_key = request.GET.get('new_video_key')
    playlist_id   = request.GET.get('id')
    return HttpResponseRedirect(reverse('player', args=[playlist_id]) + '?new_video_key=' + new_video_key)


def next_video(request):

    new_video_key   = request.GET.get('new_video_key')
    id              = request.GET.get('id')
    if new_video_key == None:
        flag = True
        df              = pd.read_csv(r'LearnHub\data\video_list.csv')
        new_df          = df[df['playlist_id'] == id]

        video_str       = new_df['video_list'].values[0]
        video_list      = ast.literal_eval(video_str)

        
        return HttpResponse(flag)
    # return render(request,'./index.html')


def quiz(request):
    
    df = pd.read_csv(r'LearnHub\data\quiz.csv')

    main_dict = df.to_dict()
    q = main_dict['question_dict']

    o = main_dict['options_dict']

    new_dict = {}

    for x in o:
        new_dict[q[x]] = ast.literal_eval(o[x])


    
    return render(request,'./quiz.html',{'ques':new_dict}) 
    # return HttpResponse(quesiton_dict['Q0'])

