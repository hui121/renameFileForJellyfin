'''
jellyfin 剧集命名工具
2024.09.07  V0.0.0
'''
import tkinter as tk  
from tkinter import filedialog  
import renameForEpisode as rfe
class GUIApp:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("处理剧集")  
        #
        self.folder_selected = None #处理文件夹
        self.name = '' #剧集名字
        self.season_number = 1
        self.episode_start = 1
        # 创建Frame来组织控件  
        self.frame       = tk.Frame(self.root) 
        self.frame_entry = tk.Frame(self.root)
        self.frame_bt    = tk.Frame(self.root)
        self.frame.grid(row=0, column = 0, padx=10, pady=10)  
        self.frame_entry.grid(row=1, column = 0, padx=10, pady=10)  
        self.frame_bt.grid(row=2, column = 0, padx=10, pady=10) 
        # 第一行  创建选择文件夹的按钮  
        self.btn_select_folder = tk.Button(self.frame, text="选择路径", command=self.select_folder)          
        self.btn_select_folder.pack(side=tk.LEFT, padx=(0, 20), pady=10)  
        # 创建用于输入剧名的Entry控件和标签 
        self.select_folder_var = tk.StringVar()  
        self.select_folder_entry = tk.Entry(self.frame, width=40, textvariable = self.select_folder_var)
        self.select_folder_entry.pack(side=tk.LEFT, padx=(0, 20), pady=10) 
        # 第二行  创建用于输入剧名的Entry控件和标签  
        self.label_tv_name = tk.Label(self.frame_entry, text="剧名")  
        #elf.label_tv_name.grid(row=1, column = 0, padx=(0, 20), pady=10) 
        self.label_tv_name.pack(side=tk.LEFT, pady=10)  
        self.tv_name_entry = tk.Entry(self.frame_entry, width=10)  
        #self.tv_name_entry.grid(row=1, column = 1, padx=(0, 20), pady=10) 
        self.tv_name_entry.pack(side=tk.LEFT, padx=(0, 20), pady=10)  
        #        创建用于输入季的Entry控件和标签  
        self.label_season_number = tk.Label(self.frame_entry, text="季")  
        #self.label_season_number.grid(row=1, column = 2, padx=(0, 20), pady=10) 
        self.label_season_number.pack(side=tk.LEFT, pady=10)  
        self.season_number_var = tk.StringVar()  # 设置默认数值为1
        self.season_number_var.set("1")
        self.season_number_entry = tk.Entry(self.frame_entry, width=10, textvariable = self.season_number_var)  
        #self.season_number_entry.grid(row=1, column = 3, padx=(0, 20), pady=10) 
        self.season_number_entry.pack(side=tk.LEFT, padx=(0, 20), pady=10)  
        #        创建用于输入集起始的Entry控件和标签  
        self.label_epi_number = tk.Label(self.frame_entry, text="集起始")  
        #self.label_epi_number.grid(row=1, column = 4, padx=(0, 20), pady=10) 
        self.label_epi_number.pack(side=tk.LEFT, pady=10)  
        self.epi_number_var = tk.StringVar()  # 设置默认数值为1
        self.epi_number_var.set("1")
        self.epi_number_entry = tk.Entry(self.frame_entry, width=10, textvariable = self.epi_number_var)  
        #self.epi_number_entry.grid(row=1, column = 5, padx=(0, 20), pady=10) 
        self.epi_number_entry.pack(side=tk.LEFT, padx=(0, 30), pady=10)  
        # 第三行  处理按钮
        self.btn_start_processing_rename = tk.Button(self.frame_bt, text="处理", command=self.start_processing_rename) 
        #self.btn_start_processing_rename.grid(row=2, column = 0, padx=(0, 20), pady=10) 
        self.btn_start_processing_rename.pack(side=tk.LEFT, padx=(20, 20), pady=10)  
        self.btn_start_processing_restore = tk.Button(self.frame_bt, text="恢复", command=self.start_processing_restore)  
        #self.btn_start_processing_restore.grid(row=2, column = 1, padx=(0, 20), pady=10) 
        self.btn_start_processing_restore.pack(side=tk.LEFT, padx=(20, 20), pady=10)  
  
    def select_folder(self):  
        self.folder_selected = filedialog.askdirectory()  
        print("Selected Folder:", self.folder_selected)     
        self.select_folder_var.set(self.folder_selected)
        
        
    def start_processing_rename(self):  
        try:  
            self.name = self.tv_name_entry.get().strip()
            # 检查文本是否为空  
            if not self.name:  
                # 如果为空，显示提示信息  
                tk.messagebox.showerror("错误", "剧名不能为空！") 
                return
            print(f"剧名: {self.name}")  
            self.season_number = int(self.season_number_entry.get())  
            print(f"季: {self.season_number}")  
            self.episode_start = int(self.epi_number_entry.get())  
            print(f"起始集: {self.episode_start}")  
            rfe.rename_files(self.folder_selected, self.name, self.season_number, self.episode_start)
            # 在这里添加你的处理逻辑，使用number变量  
        except ValueError:  
            print("命名出错")  
    def start_processing_restore(self):  
        try:
            rfe.restore_filenames(self.folder_selected)
            # 在这里添加你的处理逻辑，使用number变量  
        except ValueError:  
            print("恢复出错")  
def main():  
    root = tk.Tk()  
    app = GUIApp(root)  
    root.mainloop()  
  
if __name__ == "__main__":  
    main()