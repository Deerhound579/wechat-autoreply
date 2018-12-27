from datetime import time
from collections import defaultdict
from string import Template

course_code = [251, 302, 273, 323, 223]

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        line_count = 0
        course_names, start_times, end_times, bj_times = {}, {}, {}, {}
        # course_dict = defaultdict(list)
        for row in csv_file:
            time_list = []
            info_list = row.split(',')
            code = course_code[line_count]
            for t in info_list[1:]:
                time_list.append(
                    time(int(t.split(':')[0]), int(t.split(':')[1])))
            for tdict, t in zip([start_times, end_times, bj_times], time_list):
                tdict[code] = t

            course_names[code] = info_list[0]
            line_count += 1
        return course_names, start_times, end_times, bj_times
            # time_list = [row_spl[x] for x in range(0,4)]
            # course = row_spl[0]
            # start_time = row_spl[1]
            # end_time = row_spl[2]
            # bj_time = row_spl[3]     
            # s_time = time(int(start_time.split(':')[0]), int(start_time.split(':')[1])) # a time object
            # e_time = time(int(end_time.split(':')[0]), int(end_time.split(':')[1]))
            # b_time = time(int(end_time.split(':')[0]), int(end_time.split(':')[1]))
            # course_dict[code].extend((course, s_time, e_time))
            # course_names[code] = course
            # start_times[code] = s_time
            # end_times[code] = e_time
            # bj_times[code] = 
           

# If the file is not in the same directory
# my_dict = read_csv(os.path.relpath(os.path.join('courses_and_template', 'course_info.csv')))


def read_reply(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reply_text = f.read()
    return Template(reply_text) # Convert the text to a Template object for further substitution 
