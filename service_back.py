import requests,time,datetime

FILE_LOG = 'back_form.log'

EMAIL = 'asdtgwetwe@gmail.com'
SMTP_SERVER = 'smtp-relay.gmail.com'
SMTP_PORT = 25

SERVICE_EMAIL = 'info@a1-systems.com'

EMAIL_TRIES_GET = 2
EMAIL_TIMEOUT = 0.5

def getCountMessage(email,server,port):
    count_messages = 0
    return count_messages

def getLastMessage(email,server,port):
    sender, title, body = ('','','')
    return sender, title, body

def appendLog(list_parameters):
    file_log = open(FILE_LOG,'a')
    for parameter in list_parameters:
        file_log.write(str(parameter)+'\t')
    file_log.write('\n')
    file_log.close()
    return False

def doTest():
    messages_before_test = getCountMessage(EMAIL,SMTP_SERVER,SMTP_PORT)

    link = 'https://a1-systems.com/wp-json/contact-form-7/v1/contact-forms/656/feedback'

    correct_data = {
        'product': 'Services',
        'full-name': 'Ivanov Ivan Ivanovich',
        'email': EMAIL,
        'company': 'r_line',
        'acceptance-977': '1',
        }
    time_start_test = str(datetime.datetime.now())
    start_request = time.time()
    request = requests.post(link,data=correct_data)
    end_request = time.time()
    time_form_entered = end_request-start_request
    
    request_sended_good = request.status_code == 200
    server_entered = request.json()['status'] == 'mail_sent'

    time.sleep(2)
    tries = EMAIL_TRIES_GET
    while getCountMessage(EMAIL,SMTP_SERVER,SMTP_PORT) == messages_before_test and tries>0:
        tries -= 1
        time.sleep(EMAIL_TIMEOUT)

    message_getted = False
    if getCountMessage(EMAIL,SMTP_SERVER,SMTP_PORT) != messages_before_test:
        sender, title, body = getLastMessage(EMAIL,SMTP_SERVER,SMTP_PORT)
        if sender == SERVICE_EMAIL:
            message_getted = True
    return [time_start_test,request_sended_good,server_entered,time_form_entered,message_getted]

appendLog(doTest())
print('test ended')
