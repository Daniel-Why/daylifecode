import os
mount_ip = "start"
while mount_ip != "exit_mount":
    mount_ip = input("mount_dir:")
    command = "mount //"+mount_ip[9:]+"/share -o username=Administrator,password='!qaz2wsx#',dir_mode=0777,file_mode=0777,iocharset=utf8 "+mount_ip
    print(command)
    os.system(command)