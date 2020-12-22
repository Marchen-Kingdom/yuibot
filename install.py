import stat
from pathlib import Path

import requests

GOCQHTTP_URL = "https://github.com/Mrs4s/go-cqhttp/releases/download/v0.9.35-fix1/go-cqhttp-v0.9.35-fix1-linux-amd64"
GOCQHTTP_NAME = "go-cqhttp"


print("Installing go-cqhttp from GitHub...")
r = requests.get(GOCQHTTP_URL, allow_redirects=True)
open(GOCQHTTP_NAME, 'wb').write(r.content)
p = Path(f"./{GOCQHTTP_NAME}")
p.chmod(p.stat().st_mode | stat.S_IEXEC)
