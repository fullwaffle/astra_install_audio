## Systemd Service
```
[Unit]
Description=Install Audio
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
ExecStart=python3 /home/administrator/main.py

[Install]
WantedBy=multi-user.target
```
