import psutil
import smtplib
from email.mime.text import MIMEText
import datetime

# 告警阈值
CPU_THRESHOLD = 80  # CPU使用率超过80%时告警
MEMORY_THRESHOLD = 80  # 内存使用率超过80%时告警

# 邮件配置
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SENDER_EMAIL = "your-email@example.com"
SENDER_PASSWORD = "your-password"
RECEIVER_EMAIL = "admin@example.com"

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print(f"[{datetime.datetime.now()}] Alert sent: {subject}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Failed to send alert: {e}")

def check_resources():
    # 检查CPU使用率
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%")

    # 检查内存使用率
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        send_alert("High Memory Usage Alert", f"Memory usage is at {memory_usage}%")

if __name__ == "__main__":
    print(f"[{datetime.datetime.now()}] Monitoring started...")
    check_resources()
