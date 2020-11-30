import pandas as pd
import datetime
import win10toast

# toaster.show_toast('Python', task, duration=10)

if __name__ == "__main__":
    df = pd.read_excel('database.xlsx')
    notifier = win10toast.ToastNotifier()
    # print (df)
    # today = datetime.datetime.now().strftime("%d-%m")
    # print (today)
    now = datetime.datetime.now().strftime("%H:%M")
    # print (now)
    for index, item in df.iterrows():
        remTime = item['Time'].strftime("%H:%M")
        # print (remTime)
        # print (type (remTime))
        if (now == remTime):
            notifier.show_toast('Python', item['Task'], duration = 10)
            # remTime.delete
  