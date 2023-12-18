"""
本代码由[Tkinter布局助手]生成
当前版本:2.5.3
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_table_lqajms2p = self.__tk_table_lqajms2p()
        self.tk_label_frame_addgroup = Frame_addgroup(self)
        self.tk_label_frame_log = Frame_log(self)

    def __win(self):
        self.title("简易服务器管理器")
        # 设置窗口大小、居中
        width = 800
        height = 600
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_table_lqajms2p(self):
        # 表头字段 表头宽度
        columns = {"ID":76,"服务名":152,"命令行":532,"pid":152}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        # 插入数据示例
        # data = [
        #     [1, "github", "https://github.com/iamxcd/tkinter-helper"],
        #     [2, "演示地址", "https://www.pytk.net/tkinter-helper"]
        # ]
        #
        # # 导入初始数据
        # for values in data:
        #     tk_table.insert('', END, values=values)
        
        tk_table.place(x=20, y=160, width=760, height=241)
        return tk_table

class Frame_addgroup(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_lqakm9oe = self.__tk_label_lqakm9oe()
        self.tk_select_box_server_group = self.__tk_select_box_server_group()
        self.tk_label_lqakq2rg = self.__tk_label_lqakq2rg()
        self.tk_input_process_name = self.__tk_input_process_name()
        self.tk_label_server_ports = self.__tk_label_server_ports()
        self.tk_input_process_ports = self.__tk_input_process_ports()
        self.tk_label_server_cmd = self.__tk_label_server_cmd()
        self.tk_input_process_cmd = self.__tk_input_process_cmd()
        self.tk_button_process_add = self.__tk_button_process_add()
        self.tk_button_process_update = self.__tk_button_process_update()
        self.tk_button_process_del = self.__tk_button_process_del()
        self.tk_button_process_copy = self.__tk_button_process_copy()
        self.tk_button_group_save = self.__tk_button_group_save()
        self.tk_button_group_del = self.__tk_button_group_del()
        self.tk_button_group_copy = self.__tk_button_group_copy()
        self.tk_button_start = self.__tk_button_start()
        self.tk_button_stop = self.__tk_button_stop()
        self.tk_button_update_and_start = self.__tk_button_update_and_start()
    def __frame(self):
        self.configure(text="添加组")
        self.place(x=20, y=0, width=757, height=148)

    def __tk_label_lqakm9oe(self):
        label = Label(self,text="服务组",anchor="center")
        label.place(x=20, y=10, width=50, height=24)
        return label

    def __tk_select_box_server_group(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("列表框","Python","Tkinter Helper")
        cb.place(x=80, y=10, width=150, height=24)
        return cb

    def __tk_label_lqakq2rg(self):
        label = Label(self,text="服务名",anchor="center")
        label.place(x=20, y=40, width=50, height=24)
        return label

    def __tk_input_process_name(self):
        ipt = Entry(self)
        ipt.place(x=80, y=40, width=150, height=24)
        return ipt

    def __tk_label_server_ports(self):
        label = Label(self,text="端口号：",anchor="center")
        label.place(x=250, y=40, width=50, height=24)
        return label

    def __tk_input_process_ports(self):
        ipt = Entry(self)
        ipt.place(x=320, y=40, width=150, height=24)
        return ipt

    def __tk_label_server_cmd(self):
        label = Label(self,text="命令行",anchor="center")
        label.place(x=20, y=70, width=50, height=24)
        return label

    def __tk_input_process_cmd(self):
        ipt = Entry(self)
        ipt.place(x=80, y=70, width=391, height=24)
        return ipt

    def __tk_button_process_add(self):
        btn = Button(self, text="添加")
        btn.place(x=20, y=100, width=50, height=24)
        return btn

    def __tk_button_process_update(self):
        btn = Button(self, text="修改")
        btn.place(x=80, y=100, width=50, height=24)
        return btn

    def __tk_button_process_del(self):
        btn = Button(self, text="删除")
        btn.place(x=140, y=100, width=50, height=24)
        return btn

    def __tk_button_process_copy(self):
        btn = Button(self, text="复制")
        btn.place(x=200, y=100, width=50, height=24)
        return btn

    def __tk_button_group_save(self):
        btn = Button(self, text="保存服务组")
        btn.place(x=480, y=0, width=75, height=50)
        return btn

    def __tk_button_group_del(self):
        btn = Button(self, text="删除服务组")
        btn.place(x=560, y=0, width=75, height=50)
        return btn

    def __tk_button_group_copy(self):
        btn = Button(self, text="复制服务组")
        btn.place(x=640, y=0, width=75, height=50)
        return btn

    def __tk_button_start(self):
        btn = Button(self, text="启动组")
        btn.place(x=480, y=60, width=75, height=50)
        return btn

    def __tk_button_stop(self):
        btn = Button(self, text="关闭组")
        btn.place(x=560, y=60, width=75, height=50)
        return btn

    def __tk_button_update_and_start(self):
        btn = Button(self, text="更新重启")
        btn.place(x=640, y=60, width=75, height=50)
        return btn

class Frame_log(LabelFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_tabs_lqalgqkt = Frame_lqalgqkt(self)
    def __frame(self):
        self.configure(text="日志区域")
        self.place(x=20, y=410, width=757, height=190)

class Frame_lqalgqkt(Notebook):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):

        self.tk_tabs_lqalgqkt_0 = Frame_lqalgqkt_0(self)
        self.add(self.tk_tabs_lqalgqkt_0, text="选项卡1")

        self.tk_tabs_lqalgqkt_1 = Frame_lqalgqkt_1(self)
        self.add(self.tk_tabs_lqalgqkt_1, text="选项卡2")

        self.place(x=0, y=-1, width=756, height=176)

class Frame_lqalgqkt_0(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):
        self.place(x=0, y=-1, width=756, height=176)

class Frame_lqalgqkt_1(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
    def __frame(self):
        self.place(x=0, y=-1, width=756, height=176)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.config(menu=self.create_menu())
        self.__event_bind()

    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_command(label="菜单1",command=self.on_menu_1)
        return menu
    def on_menu_1(self):
        print("点击了菜单")
        
    def on_server_group_select(self,evt):
        print("<<ComboboxSelected>>事件未处理",evt)
        
    def on_server_process_update(self,evt):
        print("<Button>事件未处理",evt)
        
    def on_server_process_del(self,evt):
        print("<Button>事件未处理",evt)
        
    def on_server_process_copy(self,evt):
        print("<Button>事件未处理",evt)
        
    def __event_bind(self):
        self.tk_label_frame_addgroup.tk_label_server_ports.bind('<<ComboboxSelected>>',self.on_server_group_select)
        self.tk_label_frame_addgroup.tk_button_process_update.bind('<Button>',self.on_server_process_update)
        self.tk_label_frame_addgroup.tk_button_process_del.bind('<Button>',self.on_server_process_del)
        self.tk_label_frame_addgroup.tk_button_process_copy.bind('<Button>',self.on_server_process_copy)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
