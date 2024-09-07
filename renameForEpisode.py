import os    
def rename_files(directory, name, season_number = 1, episode_start = 1):  
    # 确保输入的是目录  
    if not os.path.isdir(directory):  
        print(f"Error: {directory} is not a directory.")  
        return  
  
    # 获取所有文件的列表，并排除子目录  
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.vob', '.3gp']      
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and 'original_filenames.txt' != f and any(f.lower().endswith(ext) for ext in video_extensions)]  
  
    # 检查是否有文件需要重命名  
    if not files:  
        print("No files to rename.")  
        return  
    for filename in files:  
        print(filename)
    dorename = input('是否开始重命名，输入y开始，输入n取消')    
    if dorename == 'y':
        # 保存原始文件名到文件  
        ori_file = os.path.join(directory, "original_filenames.txt")
        if os.path.exists(ori_file):  
            print( "original_filenames.txt已存在，文件夹可能已经重命名，确认后再执行。")
            return
        file = open(ori_file, "w")
        # 按照sXXeYY的格式重命名文件  
        for i, filename in enumerate(files, start=episode_start):  
                # 计算集数，每季假设有100集（可根据实际情况调整）  
                episode = i
          
                # 格式化新的文件名  
                new_filename = f"{name}.s{season_number:02d}e{episode:02d}{os.path.splitext(filename)[1]}"  
          
                # 构建完整路径  
                old_path = os.path.join(directory, filename)  
                new_path = os.path.join(directory, new_filename)  
          
                # 重命名文件  
                os.rename(old_path, new_path)  
                print(f"Renamed {filename} to {new_filename}")  
                # 保存修改操作
                file.write(filename + ',' + new_filename+'\n')
        file.close()
        print("Renaming complete.")  
 
def restore_filenames(directory):  
    # 确保输入的是目录  
    if not os.path.isdir(directory):  
        print(f"Error: {directory} is not a directory.")  
        return  
  
    # 读取原始文件名  
    with open(os.path.join(directory, "original_filenames.txt"), "r") as file:  
        filelists = [line.strip().split(',') for line in file.readlines()]
  
    # 检查是否有文件需要恢复  
    if not filelists:  
        print("No files to restore.")  
        return  

    # 遍历原始文件名，并尝试恢复  
    for filelist in filelists:       
        original_filename = filelist[0]
        current_filename  = filelist[1]
        # 构建完整路径  
        original_path = os.path.join(directory, original_filename)  
        current_path  = os.path.join(directory, current_filename)              # 重命名文件  
        os.rename(current_path, original_path)  
    print('restore file name complete')
'''  
# 使用示例  
if __name__ == "__main__":  
    directory_path = "/path/to/your/directory"  # 修改为你的文件夹路径  
    rename_files(directory_path, season=1)  # 你可以指定起始季数'''