import tkinter as tk
from tkinter import messagebox
#import math

window = tk.Tk()
window.title('BMI')
window.geometry('600x480')
window.configure(background='YellowGreen')

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())
        bmi = round(float(weight) / (float(height)/100)**2,2)
        result = '你的 BMI 指數為：{} {}'.format(bmi, total_bmi(bmi))
        result_label.configure(text=result)
    except:
        tk.messagebox.showwarning(title='嘿', message='輸入數字好不')
        height_entry.delete(0, 'end')
        weight_entry.delete(0, 'end')


def total_bmi(bmi):
    if bmi < 10 or bmi > 40:
        return '搞啥 你輸入錯了吧'
    elif bmi >= 10 and bmi <18.5:
        return '你不胖'
    elif bmi >= 18.5 and bmi < 24:
        return '你不算胖'
    elif bmi >= 24:
        return '你胖'

header = tk.Label(window, text='BMI 計算器', fg='BLUE')
header.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（cm）', fg='BLUE')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）', fg='BLUE')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate = tk.Button(window, text='計算', command=calculate_bmi, fg='Red')
calculate.pack()

window.mainloop()
####################################################################################################################
a=int(input("邊長一:"))    #第一條邊
b=int(input("邊長二:"))   #第二條邊
c=int(input("邊長三:"))    #第三條邊
if (a+b>c) and (a+c>b) and (b+c>a):             #三角形判斷
    if a==b==c:
        print("正三角形") #等邊三角形
    elif (a==b or a==c or b==c):
        print("等腰三角形")
    elif (a*a+b*b==c*c) or (a*a+b*b==c*c) or (a*a+b*b==c*c):
        print("直角三角形")
    else:
        print("三角形")
else :
    print("這不是三角形")
####################################################################################################################
import tkinter as tk
from tkinter import filedialog
window = tk.Tk()
window.geometry("500x300")
def open_file():
    filename = filedialog.askopenfilename(title='開啟png檔案', filetypes=[('png', '*.png')])
    entry_filename.insert('insert', filename)

button_import = tk.Button(window, text="匯入檔案", command=open_file).pack()

entry_filename = tk.Entry(window, width=30, font=("宋體", 10, 'bold'))
entry_filename.pack()

def print_file():               # 輸出
    print(entry_filename.get())
tk.Button(window, text="輸出", command=print_file).pack()
window.mainloop()