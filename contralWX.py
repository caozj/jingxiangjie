from  zhuanlian import ZhuanLian
import time
from wxpy import *
bot = Bot()
print(bot.groups())
my_groups = bot.groups().search('JD优惠信息促销')


him_groups=bot.groups().search('京东')
print(my_groups)
print(him_groups)

@bot.register(him_groups)
def sync_my_groups(msg):
    print(msg)
    if msg.type =='Picture':
        for my_group in my_groups:
            msg.forward(my_group)
            time.sleep(2)
        # print(os.getcwd()+"\img\\"+msg.file_name)
        # msg.get_file(save_path=os.getcwd()+"\img\\"+msg.file_name)
        # my_friend.send_image(os.getcwd()+"\img\\"+msg.file_name)
    elif msg.type =='Text':
        for my_group in my_groups:
            content = ZhuanLian(msg)
            url_content = content.urlTransform()
            my_content = content.zhuan(url_content)
            print(my_content)
            my_group.send(my_content)
            time.sleep(2)

#堵塞线程，让机器人保持运行
bot.join()

# while 1==1:
#     sync_my_groups
