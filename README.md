# 服务器监控系统 (Server Monitor)

## 项目概述
在某公司实习期间，我开发了一套服务器监控系统，用于实时监控服务器的CPU、内存和磁盘使用情况，目标是及时发现潜在问题并发送告警。

## 技术栈
- **操作系统**: CentOS 7  
- **虚拟化**: VMware Workstation Pro  
- **语言**: Python, Shell  

## 实现过程
- 编写Python脚本（`monitor.py`），使用`psutil`库监控CPU和内存使用率。  
- 编写Shell脚本（`check_disk.sh`），使用`df -h`检查磁盘使用情况。  
- 设置告警阈值（CPU/内存>80%时发送邮件，磁盘>80%时输出告警）。  
- 使用`crontab`定时运行脚本，每5分钟检查一次：  
  ```bash
  */5 * * * * /root/server-monitor/monitor.py
  */5 * * * * /root/server-monitor/check_disk.sh
