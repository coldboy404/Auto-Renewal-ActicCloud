import requests
import re
import json
import time
import random
import os
from datetime import datetime, timedelta
import base64

# 临时方案：忽略目标站点的 HTTPS 证书校验（证书过期会导致 workflow 直接失败）
# 注意：这会降低安全性，建议后续替换为可控域名或修复证书后再开启校验。
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def _0x1a2b():
    if os.environ.get('CONFIG'):
        return json.loads(os.environ.get('CONFIG'))
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

_0x3c4d = _0x1a2b()
_0x5e6f = base64.b64decode('aHR0cHM6Ly92cHMucG9sYXJiZWFyLm55Yy5tbg==').decode()
_0x7g8h = requests.Session()
# 临时方案：忽略 HTTPS 证书校验（用于绕过对方站点证书过期问题）
_0x7g8h.verify = False
_0x7g8h.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9",
})

_0x9i0j = []

def log(msg):
    print(msg)
    _0x9i0j.append(msg)

def _0x1k2l(message):
    _0xa = _0x3c4d.get('telegram_bot_token', '')
    _0xb = _0x3c4d.get('telegram_chat_id', '')
    if not _0xa or not _0xb:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{_0xa}/sendMessage",
            data={"chat_id": _0xb, "text": message, "parse_mode": "HTML"},
            timeout=10
        )
    except:
        pass

def _0x3m4n():
    _0x7g8h.get(f"{_0x5e6f}{base64.b64decode('L2luZGV4L2xvZ2luLz9yZWZlcmVyPQ==').decode()}", timeout=10)
    _0xc = _0x7g8h.post(
        f"{_0x5e6f}{base64.b64decode('L2luZGV4L2xvZ2luLz9yZWZlcmVyPQ==').decode()}",
        data={"swapname": _0x3c4d['username'], "swappass": _0x3c4d['password']},
        headers={"Origin": _0x5e6f, "Referer": f"{_0x5e6f}{base64.b64decode('L2luZGV4L2xvZ2luLz9yZWZlcmVyPQ==').decode()}"},
        timeout=10, allow_redirects=True
    )
    return "success=" in _0xc.url or any(x in _0xc.text for x in [base64.b64decode('55m75pmG5oiQ5Yqf').decode(), base64.b64decode('5qyi6L+O5Zue5p2l').decode(), base64.b64decode('5o6n5Yi26Z2i5p2/').decode()])

def _0x5o6p(_0xd):
    _0xe = _0x7g8h.get(f"{_0x5e6f}{base64.b64decode('L2NvbnRyb2wvZGV0YWlsLw==').decode()}{_0xd}/", timeout=10)
    _0xf = re.search(base64.b64decode('5Yiw5pyf5pe26Ze0PC90aD5ccyo8dGQ+XHMqKFswLTldezR9LVswLTldezJ9LVswLTldezJ9KVxzKjwvdGQ+').decode(), _0xe.text)
    if not _0xf:
        raise RuntimeError("无法解析到期时间")
    return _0xf.group(1).strip()

def _0x7q8r(_0xd):
    _0x10 = _0x5o6p(_0xd)
    _0x11 = _0x7g8h.post(
        f"{_0x5e6f}{base64.b64decode('L2NvbnRyb2wvZGV0YWlsLw==').decode()}{_0xd}{base64.b64decode('L3BheS8=').decode()}", data={},
        headers={"Origin": _0x5e6f, "Referer": f"{_0x5e6f}{base64.b64decode('L2NvbnRyb2wvZGV0YWlsLw==').decode()}{_0xd}/"},
        timeout=10, allow_redirects=True
    )
    _0x12 = _0x5o6p(_0xd)
    _0x13 = "success=" in _0x11.url or base64.b64decode('5YWN6LS55Lqn5ZOB5bey57uP5biu5oKo57ut5pyf').decode() in _0x11.text
    return {'success': _0x13, 'before': _0x10, 'after': _0x12, 'changed': _0x10 != _0x12}

def _0x9s0t(_0x14):
    try:
        # 运行计划：最少间隔 2 天，最多间隔 4 天
        # 每次运行都会随机一个间隔，并写回 workflow 的 cron
        if not _0x14:
            _0x15 = datetime.now() + timedelta(days=7)
            _0x16 = 7
        else:
            _0x15 = datetime.strptime(_0x14, "%Y-%m-%d")
            _0x16 = (_0x15 - datetime.now()).days
        
        _0x17 = random.randint(2, 4)
        
        _0x18 = random.randint(6, 22)
        _0x19 = random.randint(0, 59)
        _0x1a = f"{_0x19} {_0x18} */{_0x17} * *"
        
        _0x1b = datetime.now() + timedelta(days=_0x17)
        _0x1b = _0x1b.replace(hour=_0x18, minute=_0x19, second=0)
        _0x1c = _0x1b + timedelta(hours=8)
        
        log(f"\n📅 更新运行计划:")
        log(f"   到期日期: {_0x14}, 剩余 {_0x16} 天")
        log(f"   运行间隔: 每 {_0x17} 天")
        log(f"   下次运行: {_0x1c.strftime('%Y-%m-%d %H:%M')} (北京时间)")
        
        _0x1d = '.github/workflows/auto-renewal.yml'
        with open(_0x1d, 'r', encoding='utf-8') as f:
            _0x1e = f.read()
        _0x1f = re.sub(r"- cron: '[^']*'", f"- cron: '{_0x1a}'", _0x1e, count=1)
        with open(_0x1d, 'w', encoding='utf-8') as f:
            f.write(_0x1f)
        log(f"   ✅ Workflow 已更新")
        return True
    except Exception as e:
        log(f"   ⚠️ 更新失败: {e}")
        return False

def main():
    _0x20 = datetime.now()
    log(f"🚀 ArcticCloud续期任务启动")
    log(f"开始时间: {_0x20.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if not _0x3m4n():
        log("❌ 登录失败")
        _0x1k2l("\n".join(_0x9i0j))
        return
    
    _0x21 = _0x22 = 0
    _0x23 = None
    
    for _0x24 in _0x3c4d['product_ids']:
        try:
            _0x25 = _0x7q8r(_0x24)
            if _0x25['success']:
                _0x26 = f"从 {_0x25['before']} 到 {_0x25['after']}" if _0x25['changed'] else f"到期: {_0x25['after']}, 已达最大续期"
                log(f"✅ 产品 {_0x24} 续费成功 ({_0x26})")
                _0x21 += 1
                if not _0x23 or _0x25['after'] < _0x23:
                    _0x23 = _0x25['after']
            else:
                log(f"⚠️ 产品 {_0x24} 续费未生效 (到期: {_0x25['before']})")
                log(f"   手动: {_0x5e6f}{base64.b64decode('L2NvbnRyb2wvZGV0YWlsLw==').decode()}{_0x24}/")
                _0x22 += 1
        except Exception as e:
            log(f"❌ 产品 {_0x24} 失败: {e}")
            log(f"   手动: {_0x5e6f}{base64.b64decode('L2NvbnRyb2wvZGV0YWlsLw==').decode()}{_0x24}/")
            _0x22 += 1
        
        if len(_0x3c4d['product_ids']) > 1 and _0x24 != _0x3c4d['product_ids'][-1]:
            time.sleep(2)
    
    if _0x23:
        _0x9s0t(_0x23)
    
    _0x27 = int((datetime.now() - _0x20).total_seconds())
    log(f"\n结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log(f"总耗时: {_0x27} 秒")
    log(f"📊 统计: 成功 {_0x21}, 失败 {_0x22}")
    
    _0x1k2l("\n".join(_0x9i0j))

if __name__ == "__main__":
    main()
