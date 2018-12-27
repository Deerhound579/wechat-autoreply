#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time as ti
import schedule
from wxpy import *
from datetime import time, date
from info_reader import read_csv, read_reply 

bot = Bot(cache_path=True, console_qr=True)
bot.enable_puid('wxpy_puid.pkl')

# At first, I wanted a dictionary like {course_code: [NAME, START_TIME, END_TIME]}. 
# For example, {251: ['数据结构与算法', 13:05, 14:25]}
# But I think access the name like course[251], time like start_time[251] is more intuitive
course_names, s_times, e_times, b_times = read_csv('course_info.csv')
reply_msg = read_reply('reply_template.txt')

# Initialize users to reply
reply_to = ['葛雨菲', '渣渣瑶', '广柑精', '老汉', '婆婆']
test_usr = ['里斯先']
user_list = [ensure_one(bot.friends().search(name)) for name in reply_to]
test_list = [ensure_one(bot.friends().search(name)) for name in test_usr]

# Below is what I did at first, but I realized it was repetitive and boring.
# mygege = ensure_one(bot.friends().search('葛雨菲'))
# xiaozhang = ensure_one(bot.friends().search('渣渣瑶'))
# mom = ensure_one(bot.friends().search('广柑精'))
# dad = ensure_one(bot.friends().search('老汉'))

mon_wed_crs = [302, 223]
tue_thur_crs = [323, 251, 273]
fri_crs = [223] 

day_course_dict = {0:mon_wed_crs, 1:tue_thur_crs, 2:mon_wed_crs, 3:tue_thur_crs, 4:fri_crs}

def test(day, cur_time):
    if day in day_course_dict:
        print(f'Today is {day}')
        today_courses = day_course_dict.get(day)
        for c in today_courses:
            # Determine which time interval it is, and return the course
            if time(17,37) <= cur_time <= time(22,20):
                print(reply_msg.substitute(
                                           COURSE=course_names[c], 
                                           ENDTIME=e_times[c].strftime('%H:%M'),
                                           BJTIME=b_times[c].strftime('%H:%M'))
                                           )
                return reply_msg.substitute(
                                            COURSE=course_names[c],
                                            ENDTIME=e_times[c].strftime('%H:%M'),
                                            BJTIME=b_times[c].strftime('%H:%M')
                                           )

def find_course(day, cur_time):
    '''
        day is an integer, cur_time is a time object.
        This function is to find the course, given the day and time.
        It returns the reply message after substitution
    '''
    # If it's not a weekday, do nothing
    if day not in day_course_dict:
        return
    today_courses = day_course_dict.get(day)
    for c in today_courses:
        if s_times[c] <= cur_time <= e_times[c]: # Determine which time interval it is, and return the course
            return reply_msg.substitute(
                                        COURSE=course_names[c],
                                        ENDTIME=e_times[c].strftime('%H:%M'),
                                        BJTIME=b_times[c].strftime('%H:%M')
                                        )
    return

# Bad idea. Too many repetitive lines. I keep it here for comparison.
# if day==0 or day==2: # Monday or Wednesday
#     for c in mon_wed_crs:
#         if s_times[c]<=cur_time<=e_times[c]:
#             return reply_msg.substitute(COURSE=course_names[c], ENDTIME=e_times[c])
# elif day==1 or day==3: # Thursday or 
#     for c in tue_thur_crs:
#         if s_times[c] <= cur_time <= e_times[c]:
#             return reply_msg.substitute(COURSE=course_names[c], ENDTIME=e_times[c])

# For all message types
@bot.register(except_self=False)
def reply_mycourse(msg):
    today = date.today().weekday() # Monday is 0
    r_time = msg.receive_time
    rec_time = time(r_time.hour, r_time.minute) # Create a time object for comparison
    
    # if msg.sender not in user_list: # Check if the sender is from the user list
    #     return
    
    # reply = find_course(today, rec_time)
    # return reply
    if msg.sender in test_list:
        bot.file_helper.send(test(today, rec_time))
        # test(today, rec_time)
    
    
embed()
