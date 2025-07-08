import os
import shutil

# 获取系统变量
systemDrive = os.environ.get('systemdrive') + '\\'
winDir = os.environ.get('windir')
userProfile = os.environ.get('userprofile')

# 要删除的文件后缀
filesDict = {
    systemDrive: ['.tmp', '._mp', '.log', '.gid', '.chk', '.old'],
    winDir: ['.bak']
}
# 要清空的文件夹
directoriesDict = {
    systemDrive: ['recycled'],
    winDir: ['prefetch', 'temp'],
    userProfile: ['cookies', 'recent',
                  'Local Settings\\Temporary Internet Files',
                  'Local Settings\\Temp']
}

def delete_files():
    for path, exts in filesDict.items():
        for root, _, files in os.walk(path):
            for file in files:
                for ext in exts:
                    if file.endswith(ext):
                        file_path = os.path.join(root, file)
                        try:
                            print(f"删除文件: {file_path}")
                            os.remove(file_path)
                        except Exception as e:
                            print(f"删除失败: {file_path}，原因: {e}")

def delete_dirs():
    for path, dirs in directoriesDict.items():
        for d in dirs:
            dir_path = os.path.join(path, d)
            if os.path.exists(dir_path):
                try:
                    print(f"删除文件夹: {dir_path}")
                    shutil.rmtree(dir_path)
                except Exception as e:
                    print(f"删除失败: {dir_path}，原因: {e}")

if __name__ == '__main__':
    delete_files()
    delete_dirs()
    print("清理完成")
    os.system('pause')