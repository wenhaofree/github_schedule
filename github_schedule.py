"""
1. 定时触发
2. 文件写入日期
3. 自动提交
"""

import os
import time
import datetime
import schedule
import subprocess
def main():
    # 写入当前目录的json文件
    now = datetime.datetime.now()
    file_path = os.path.join(os.path.dirname(__file__), "data.txt")
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(now_str)
        f.write("\n")
        print(now_str)
    # 触发脚本命令
    file_path = os.path.join(os.path.dirname(__file__), "git.sh")
    command=f'sh {file_path}'
    subprocess.call(command, shell=True)
    print("提交成功")

def schedule_job():
    # schedule.every().day.at("08:00").do(main)
    # schedule.every().day.at("10:42").do(job)
    # schedule.every(1).seconds.do(job)
    schedule.every(1).minutes.do(main)
    # schedule.every(1).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    print('[程序启动...]')
    schedule_job()