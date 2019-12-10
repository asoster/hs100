#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  utils.py
#
#  Copyright 2019 https://github.com/asoster
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


import yaml

import socket

from codecs import decode


def read_config(file_name):
    with open(file_name, 'rt', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def shutdown_request(config):
    if config['debug']:
        config['ip'] = '127.0.0.1'
    print(config['sutdown_msg'])
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((config['ip'], config['port']))
    for data in config['shutdown_seq']:
        ss.send(decode(data['data'], data['codec']))
    ss.close()


def start_request(config):
    if config['debug']:
        config['ip'] = '127.0.0.1'
    print(config['start_msg'])
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((config['ip'], config['port']))
    for data in config['start_seq']:
        ss.send(decode(data['data'], data['codec']))
    ss.close()
