import os
import time
import subprocess 
import atexit                                              

dir_path = os.path.dirname(os.path.realpath(__file__)) + "/.."            
                                                                
vfirm_dir = dir_path + "/Virtual-Firmware-grSim"
vfirm_cmd = "./vfirm.exe"
vfirm_port_base = 8000
vfirm_is_blue = "1"

tritonBot_dir = dir_path + "/TritonBot/build/"
tritonBot_cmd = "./TritonBot.exe"
tritonBot_virtual = "-v"
tritonBot_port_base_base = 6000

def run_cmd_term(cmd, cwd):
    print("opening new terminal with command: " + ' '.join(map(str, cmd))  + " at " + cwd)
    subprocess.Popen(["gnome-terminal", "--tab", "--"] + cmd, cwd=cwd)                                                   

def clear_ports():
    for i in range(0, 6):
        vfirm_port = str(vfirm_port_base + i * 10)
        os.system("fuser -k {port}/tcp".format(port = vfirm_port))

atexit.register(clear_ports)

clear_ports()

#time.sleep(5)
for i in range(0, 6):
    vfirm_port = str(vfirm_port_base + i * 10)
    vfirm_robot_id = str(i)
    run_cmd_term([vfirm_cmd, vfirm_port, vfirm_robot_id, vfirm_is_blue], vfirm_dir)
    time.sleep(1)

for i in range(0, 6):
    tritonBot_port_base = str(tritonBot_port_base_base + i * 100)
    vfirm_port = str(vfirm_port_base + i * 10)
    tritonBot_vfirm_port = vfirm_port
    run_cmd_term([tritonBot_cmd, tritonBot_virtual, tritonBot_port_base, tritonBot_vfirm_port], tritonBot_dir)   

while (True):
    time.sleep(100)