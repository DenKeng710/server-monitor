#!/bin/bash

# 告警阈值
DISK_THRESHOLD=80

# 检查磁盘使用率
DISK_USAGE=$(df -h / | tail -1 | awk '{print $5}' | cut -d'%' -f1)

if [ $DISK_USAGE -gt $DISK_THRESHOLD ]; then
    echo "Disk usage is at ${DISK_USAGE}% - CRITICAL"
    # 这里可以添加告警逻辑，比如发送邮件
    exit 2
else
    echo "Disk usage is at ${DISK_USAGE}% - OK"
    exit 0
fi
