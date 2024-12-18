# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    days = {'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday'}
    print(days.__class__)
    print(len(days))
    days2 = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday']
    print(days2.__class__)
    print(days2[0:2])

    days3 = ('Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday')
    print(days3.__class__)
    print(days3[0:2])
    a=1
    while a<10:
        print(a)
        a+=2
    else:
        print('a=',a)

    for day in days3:
        print(day)
    for num in range(10,20):
        for i in range(2,num):
            if num%i==0:
                j=num/i
                print('%d 等于 %d乘以%d'%(num,i,j))
                break
        else:
                print('%d是个质数'%num)

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
