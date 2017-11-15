"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""

text_number_list = []
for text_number in texts:
	text_number_list.append(text_number[0])
	text_number_list.append(text_number[1])



call_number_list = []
for call_number in calls:
	call_number_list.append(call_number[0])
	call_number_list.append(call_number[1])


phone_number_list= call_number_list + text_number_list

set(phone_number_list)

print('There are {} different telephone numbers in the records.'.format(len(phone_number_list)))