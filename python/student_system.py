'''
Author: your name
Date: 2022-04-16 14:40:15
LastEditTime: 2022-04-16 15:16:27
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Leetcode\python\student_system.py
'''
info = '''
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学信信息

0. 推出系统
'''
my_dict = []

def input_student():
    name = input('input name: ')
    total = input('input total message: ')
    dict1 = {'name': name, 'total': total}
    my_dict.append(dict1)
    return 


while True:
    print(info)
    action = int(input("输入命令: "))
    if action == 1:
        input_student()
    elif action == 2:
        for i in my_dict:
            print('name:', i['name'], 'total:', i['total'])
    elif action == 3:
        tmp_name = input('which name want to check:')
        flg = False
        for i in my_dict:
            if i['name'] == tmp_name:
                print('name:', i['name'], 'total:', i['total'])
                flg = True
                break
        if flg == False:
            print('no mamber!')        
    elif action == 4:
        tmp_name = input('which name want to delete:')
        flg = False
        for i in my_dict:
            if i['name'] == tmp_name:
                my_dict.remove(i)
                print('Success!')
                flg = True
                break
        if flg == False:
            print('no mamber!') 
    elif action == 5:
        tmp_name = input('which name want to delete:')
        flg = False
        for i in my_dict:
            if i['name'] == tmp_name:
                tmp_total = int(input('real total'))
                i['total'] = tmp_total
                print('Success!')
                flg = True
                break
        if flg == False:
            print('no mamber!') 
    elif action == 0:
        print('推出系统')
        break
    else:
        print("please input true action!")