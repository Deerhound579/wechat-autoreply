from datetime import time
from collections import defaultdict
from string import Template

course_code = [251, 302, 273, 323, 223]

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as csv_file:
        line_count = 0
        course_names, start_times, end_times = {}, {}, {}
        # course_dict = defaultdict(list)
        for row in csv_file:
            course = row.split(',')[0]
            start_time = row.split(',')[1]
            end_time = row.split(',')[2]
            s_time = time(int(start_time.split(':')[0]), int(start_time.split(':')[1])) # a time object
            e_time = time(int(end_time.split(':')[0]), int(end_time.split(':')[1]))
            code = course_code[line_count]
            # course_dict[code].extend((course, s_time, e_time))
            course_names[code] = course
            start_times[code] = s_time
            end_times[code] = e_time
            line_count +=1
        return course_names, start_times, end_times

# If the file is not in the same directory
# my_dict = read_csv(os.path.relpath(os.path.join('courses_and_template', 'course_info.csv')))


def read_reply(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reply_text = f.read()
    return Template(reply_text) # Convert the text to a Template object for further substitution 
