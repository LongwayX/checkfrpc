import os
import time
import threading

def check_frpc(to_list:bool = False)->bool:
    
    shell = "sudo systemctl status frpc@frpc"
    if "active (running)" in get_shell_output(shell,to_list):
        return True
    return False


def restart_frpc():
    
    shell = "sudo systemctl restart frpc@frpc"
    out = get_shell_output(shell,False)
    return 


def stop_frpc():

    shell = "sudo systemctl stop frpc@frpc"
    _ = get_shell_output(shell,False)
    return


def start_frpc():

    shell = "sudo systemctl start frpc@frpc"
    _ = get_shell_output(shell,False)
    return 


def get_shell_output(shell:str,to_list:bool =True):
    fd = os.popen(shell)
    out = fd.read()
    fd.close()
    if to_list:
        out = out.split()
    return out

def action(check_epoch, sleep_time, *args, **kwargs):
    # time how long you are looking forward to sleep (minutes)
    for i in range(check_epoch):
        while not check_frpc(False):
            restart_frpc()
        time.sleep(sleep_time*60)
    return 

if __name__ == '__main__':
    # start_frpc()
    action(check_epoch=5, sleep_time=5)
    
