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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字母顺序输出。
"""

call_number_list = []
answer_number_list = []
send_number_list = []
receive_number_list = []
marketer_list = []

for call_number in calls:
	call_number_list.append(call_number[0])
for answer_number in calls:
	answer_number_list.append(answer_number[1])
for send_nubmer in texts:
	send_number_list.append(send_nubmer[0])
for receive_number in texts:
	receive_number_list.append(receive_number[1])

for number in call_number_list:
	if number not in answer_number_list and number not in send_number_list and number not in receive_number_list:
		marketer_list.append(number)
set(marketer_list)
telemarketers_list = []
for number in marketer_list:
	if number[0:3] == "140":
		telemarketers_list.append(number)


print("These numbers could be telemarketers:")
for elements in telemarketers_list:
	print(elements)




