import paramiko

import os
import sys

root_folder = os.path.abspath(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
from config.init_config import config_file as config


host = config['rig_ssh_creds']['host']
username = config['rig_ssh_creds']['username']
password = config['rig_ssh_creds']['password']

# TODO use nvidia-smi for nvidia cards and rocm-smi for AMD cards.
#
# Output sample of nvidia-smi :
# Fri Sep 30 15:56:09 2022
# +-----------------------------------------------------------------------------+
# | NVIDIA-SMI 460.67       Driver Version: 460.67       CUDA Version: 11.2     |
# |-------------------------------+----------------------+----------------------+
# | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
# | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
# |                               |                      |               MIG M. |
# |===============================+======================+======================|
# |   0  GeForce RTX 3070    On   | 00000000:10:00.0  On |                  N/A |
# | 99%   59C    P2   124W / 125W |   3339MiB /  7981MiB |    100%      Default |
# |                               |                      |                  N/A |
# +-------------------------------+----------------------+----------------------+
# |   1  GeForce RTX 306...  On   | 00000000:21:00.0 Off |                  N/A |
# | 56%   55C    P2   124W / 125W |   3305MiB /  7982MiB |    100%      Default |
# |                               |                      |                  N/A |
# +-------------------------------+----------------------+----------------------+

# +-----------------------------------------------------------------------------+
# | Processes:                                                                  |
# |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
# |        ID   ID                                                   Usage      |
# |=============================================================================|
# |    0   N/A  N/A      2546      G   /usr/lib/xorg/Xorg                 18MiB |
# |    0   N/A  N/A      4202      C   ...miners/gminer/3.05/gminer     3317MiB |
# |    1   N/A  N/A      2546      G   /usr/lib/xorg/Xorg                  6MiB |
# |    1   N/A  N/A      4202      C   ...miners/gminer/3.05/gminer     3295MiB |
# +-----------------------------------------------------------------------------+
#
# output sample of rocm-smi:
#
#
# ========================ROCm System Management Interface========================
# ================================================================================
# GPU  Temp   AvgPwr   SCLK     MCLK     Fan     Perf    PwrCap  VRAM%  GPU%
# 2    56.0c  91.206W  1200Mhz  2200Mhz  45.88%  manual  155.0W   39%   100%
# 3    55.0c  81.142W  1100Mhz  2000Mhz  27.84%  manual  175.0W   81%   100%
# 4    55.0c  126.0W   1240Mhz  1049Mhz  31.76%  manual  272.0W   20%   99%
# 5    55.0c  124.0W   1240Mhz  1049Mhz  41.96%  manual  264.0W   20%   99%
# ================================================================================
# ==============================End of ROCm SMI Log ==============================


client = paramiko.client.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout, _stderr = client.exec_command("ls")
print(_stdout.read().decode())
client.close()
