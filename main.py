from daka import DaKa

import sys


def doDaka(username, password):
    print("🚌 打卡任务启动")
    dk = DaKa(username, password)
    try:
        dk.login()
    except Exception as err:
        raise Exception

    print('正在获取个人信息...')
    try:
        dk.get_info()
    except Exception as err:
        print('获取信息失败，请手动打卡，更多信息: ' + str(err))
        raise Exception

    try:
        res = dk.post()
        if str(res['e']) == '0':
            print('打卡成功')
        else:
            print(res['m'])
    except:
        print('数据提交失败')
        raise Exception


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    try:
        doDaka(username, password)
    except Exception as err:
        print(err)
        raise Exception


if __name__ == "__main__":
    main()
