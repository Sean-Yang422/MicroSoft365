import time
import winsound

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    # 提醒声音
    frequency = 2500  # 设置声音频率为 2500 Hz
    duration = 1000  # 设置声音持续时间为 1000 毫秒
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    minutes = int(input("请输入专注时长（分钟）："))
    countdown(minutes)
