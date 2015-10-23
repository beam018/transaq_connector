# -*- coding: utf-8 -*-
"""
Пример использования коннектора.
"""
from commands import *
import time


def handle_txml_message(msg):
    print msg


if __name__ == '__main__':
    try:
        initialize("logs", 3, handle_txml_message)
        print connect("test-login", "test-password", "213.247.141.133:3900")
        time.sleep(3)
        print get_history('TQBR', 'GAZP', 2, count=10)
        time.sleep(3)
    finally:
        print disconnect()
        uninitialize()
