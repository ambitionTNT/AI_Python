# python learing
# author:TNT
import time
import tkinter
import tkinter.messagebox
from threading import Thread

'''将耗时间的任务放到线程中以获得更好的用户体验。'''







def main():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(10)
            #啓動下载按钮
            tkinter.messagebox.showinfo('提示', '下载完成')
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程(主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者: zcl(v1.0)')








    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('300x250')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()
if __name__ == '__main__':
    main()