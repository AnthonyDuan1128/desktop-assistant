from tkinter import Tk, Frame, Label, StringVar, Button, messagebox, simpledialog, ttk, Menu, Text, Scrollbar, VERTICAL, END, Listbox
from services.time_service import TimeService
from services.traffic_service import TrafficService
from services.schedule_service import ScheduleService
from services.currency_service import CurrencyService
from services.search_service import SearchService
from services.web_scraper import WebScraper
from services.deepseek_service import DeepSeekService
import webbrowser

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("桌面助手")
        self.master.geometry("400x600+1000+0")  # 将窗口定位在右上角
        self.master.configure(bg="#f0f0f0")  # 浅色背景
        self.master.wm_attributes('-alpha', 0.9)  # 设置窗口透明度为90%
        self.master.overrideredirect(True)  # 隐藏窗口装饰

        self.frame = Frame(self.master, bg="#f0f0f0")
        self.frame.pack(pady=20)

        self.time_var = StringVar()
        self.time_label = Label(self.frame, textvariable=self.time_var, font=("Helvetica", 24), bg="#f0f0f0")
        self.time_label.pack(pady=10)

        self.time_service = TimeService()
        self.traffic_service = TrafficService()
        self.schedule_service = ScheduleService()
        self.currency_service = CurrencyService()
        self.search_service = SearchService()
        self.web_scraper = WebScraper()
        self.deepseek_service = DeepSeekService()

        self.update_time()
        self.setup_buttons()

        # 绑定 Esc 键
        self.master.bind("<Escape>", self.show_menu)

        # 添加聊天功能
        self.chat_text = Text(self.frame, wrap='word', height=10, width=40)
        self.chat_text.pack(pady=5)
        self.chat_text.insert(END, "欢迎使用桌面助手！\n")

        self.chat_input = StringVar()
        self.chat_entry = ttk.Entry(self.frame, textvariable=self.chat_input, width=40)
        self.chat_entry.pack(pady=5)
        self.chat_entry.bind("<Return>", self.ask_deepseek)

    def update_time(self):
        current_time = self.time_service.get_current_time()
        self.time_var.set(current_time)
        self.master.after(1000, self.update_time)  # 每秒更新一次

    def setup_buttons(self):
        style = ttk.Style()
        style.configure('TButton', font=('Helvetica', 12), padding=10)
        ttk.Button(self.frame, text="查看交通信息", command=self.display_traffic_info).pack(pady=5)
        ttk.Button(self.frame, text="管理日程", command=self.manage_schedule).pack(pady=5)
        ttk.Button(self.frame, text="货币转换", command=self.convert_currency).pack(pady=5)
        ttk.Button(self.frame, text="网络搜索", command=self.search_web).pack(pady=5)
        ttk.Button(self.frame, text="网站爬取", command=self.scrape_website).pack(pady=5)

    def display_traffic_info(self):
        location = simpledialog.askstring("输入", "请输入位置:")
        if location:
            try:
                traffic_data = self.traffic_service.get_traffic_info(location)
                messagebox.showinfo("交通信息", str(traffic_data))
            except Exception as e:
                messagebox.showerror("错误", str(e))

    def show_menu(self, event=None):
        # Check if the window is minimized
        if self.master.state() == 'iconic':
            self.master.deiconify()  # Restore the window
            self.master.overrideredirect(True)  # Re-enable overrideredirect
        else:
            menu = Menu(self.master, tearoff=0)
            menu.add_command(label="关闭", command=self.master.quit)
            menu.add_command(label="最大化", command=self.maximize_window)
            menu.post(event.x_root, event.y_root)

    def minimize_window(self):
        self.master.overrideredirect(False)  # Temporarily disable overrideredirect
        self.master.iconify()
        self.master.after(10, lambda: self.master.overrideredirect(True))  # Re-enable after a short delay

    def maximize_window(self):
        self.master.overrideredirect(False)  # Temporarily disable overrideredirect
        self.master.state('zoomed')
        self.master.after(10, lambda: self.master.overrideredirect(True))  # Re-enable after a short delay

    def ask_deepseek(self, event):
        question = self.chat_input.get()
        if question:
            self.chat_text.insert(END, f"用户: {question}\n")
            answer = self.deepseek_service.get_response(question)
            self.chat_text.insert(END, f"助手: {answer}\n")
            self.chat_input.set("")

    def manage_schedule(self):
        action = simpledialog.askstring("输入", "请输入操作 (add/view/remove/clear):")
        if action == "add":
            event = simpledialog.askstring("输入", "请输入事件:")
            if event:
                self.schedule_service.add_schedule(event)
                messagebox.showinfo("成功", "事件已添加。")
        elif action == "view":
            schedules = self.schedule_service.view_schedules()
            messagebox.showinfo("日程", "\n".join(schedules))
        elif action == "remove":
            event = simpledialog.askstring("输入", "请输入要移除的事件:")
            if event:
                self.schedule_service.remove_schedule(event)
                messagebox.showinfo("成功", "事件已移除。")
        elif action == "clear":
            self.schedule_service.clear_schedules()
            messagebox.showinfo("成功", "所有事件已清除。")
        else:
            messagebox.showerror("错误", "无效操作。")

    def convert_currency(self):
        amount = simpledialog.askfloat("输入", "请输入金额:")
        from_currency = simpledialog.askstring("输入", "请输入源货币 (例如 USD):")
        to_currency = simpledialog.askstring("输入", "请输入目标货币 (例如 EUR):")
        if amount and from_currency and to_currency:
            try:
                self.currency_service.fetch_exchange_rates()
                converted_amount = self.currency_service.convert_currency(amount, from_currency, to_currency)
                messagebox.showinfo("货币转换", f"{amount} {from_currency} = {converted_amount} {to_currency}")
            except Exception as e:
                messagebox.showerror("错误", str(e))

    def search_web(self):
        query = simpledialog.askstring("输入", "请输入搜索查询:")
        if query:
            try:
                results = self.search_service.search_bing(query)
                if results:
                    self.show_search_results(results)
                else:
                    messagebox.showinfo("搜索结果", "没有找到相关结果。")
            except Exception as e:
                messagebox.showerror("错误", str(e))

    def show_search_results(self, results):
        results_window = Tk()
        results_window.title("搜索结果")
        results_window.geometry("600x400")

        frame = Frame(results_window)
        frame.pack(fill='both', expand=True)

        scrollbar = Scrollbar(frame, orient=VERTICAL)
        scrollbar.pack(side='right', fill='y')

        text_widget = Text(frame, yscrollcommand=scrollbar.set, wrap='word')
        text_widget.pack(side='left', fill='both', expand=True)

        scrollbar.config(command=text_widget.yview)

        for result in results:
            text_widget.insert(END, result['title'] + "\n")
            button = Button(frame, text="访问链接", command=lambda url=result['url']: self.open_link(url))
            text_widget.window_create(END, window=button)
            text_widget.insert(END, "\n\n")

    def open_link(self, url):
        webbrowser.open(url)

    def scrape_website(self):
        url = simpledialog.askstring("输入", "请输入网站 URL:")
        if url:
            try:
                html_content = self.web_scraper.scrape(url)
                data = self.web_scraper.parse_data(html_content)
                messagebox.showinfo("爬取数据", "\n".join(data))
            except Exception as e:
                messagebox.showerror("错误", str(e))