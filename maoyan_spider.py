import requests
import emoji



file = open('maoyan.csv','w+',encoding='utf-8')
file.write('content,gender,id,nick,replyCount,score,upCount,userId,userLevel\n')

def write_content(data):
    content = data['content'].replace("\n"," ") #只能写100个中文字符]
    content = emoji.demojize(content)
    gender = data['gender']
    id = data['id']
    nick = emoji.demojize(data['nick'])
    replyCount = data['replyCount']
    score = data['score']
    upCount = data['upCount']
    userId = data['userId']
    userLevel = data['userLevel']
    write_data = '%s,%s,%s,%s,%s,%s,%s,%s,%s' % (
    content, gender, id, nick, replyCount, score, upCount, userId, userLevel)
    file.write(write_data + '\n')

#循环实现翻页
for offset in range(0,20000,15):
    url = f"http://m.maoyan.com/review/v2/comments.json?movieId=1211727&userId=-1&offset={offset}&limit=15&ts=0&type=3"
    r = requests.get(url)
    data_list = r.json()['data']['comments']

    for data in data_list:
        write_content(data)

file.close()
# for offset in range(0,100,10):
#     # url = "http://m.maoyan.com/mmdb/replies/comment/119042876.json?_v_=yes&offset=%s" % (offset)
#     url = f"http://m.maoyan.com/mmdb/replies/comment/119042876.json?_v_=yes&offset={offset}"
#     r = requests.get(url)
#
#     #查看响应信息
#     # print (r.json()['cmts'])
#     data_list = r.json()['cmts']
#     item_list = ['content','id','nickName','userId','userLevel']
#
#     for data in data_list:
#         write_data = '%s,%s,%s,%s,%s' % (data['content'],data['id'],data['nickName'],data['userId'],data['userLevel'])
#         # print (write_data)
#         with open('maoyan2.csv','a',encoding='utf-8') as fp:
#             fp.write(write_data+'\n')