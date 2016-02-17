#!/usr/bin/env python
#coding: utf-8

"""
usage: python parsemgz.py mgz-file.mgz
"""

import sys
from struct import unpack
import zlib

# unpack(fmt, bin)
# fmtのメモ
# < binがリトルエンディアン。先頭に付ける
# c char (1 byte), 複数なら数字を付ける。3文字の場合3c
# h short (2 bytes)
# i int (4 bytes)


def parse_header(string_):
  header_len      = unpack("<i", string_[0:4])[0]
  next_pos        = unpack("<i", string_[4:8])[0]
  compressed_data = string_[8:header_len]
  data = zlib.decompress(compressed_data, -zlib.MAX_WBITS)

  version = data[0:8]
  print version

  # F6 28 3C 41
  unknown_const = map(lambda s: hex(ord(s)), data[8:12])
  print unknown_const

  include_ai = unpack("<i", data[12:16])[0]
  print include_ai

  if include_ai == 1:
    pass
    # AIを使うリプは考えない
  else:
    pass
    # 下記は全部AIなし版

  unknown = data[16:20]
  game_speed1 = unpack("<i", data[20:24])[0]
  print "game_speed1 = %d" % game_speed1

  zero = data[24:28]
  game_speed2 = unpack("<i", data[28:32])[0]
  print "game_speed2 = %d" % game_speed2

  unknown2 = data[32:36]
  unknown3 = data[36:40]

  game_speed3 = unpack("<i", data[40:44])[0]
  print "game_speed3 = %d" % game_speed3

  unknown4 = data[44:61]

  # プレイヤー番号らしいが、識別子っぽい
  rec_player_ref = unpack("<h", data[61:63])[0]
  print "rec_player_ref = %d" % rec_player_ref

  # 地の女神を含むプレイヤー数
  num_player = unpack("<c", data[63])[0]
  print "num_player = %d" % ord(num_player)

  zero2 = data[64:68]
  negative = data[68:80]
  print "negative = ", [negative]
  unknown5 = data[80:94]
  unknown6 = data[94:126] # ゲームスピードらしいが、もういらん

  map_size_x = unpack("<i", data[126:130])[0]
  map_size_y = unpack("<i", data[130:134])[0]
  print "map_size_x, y =", map_size_x, map_size_y

  num_unknown_data = data[134:138]


if __name__ == "__main__":
  #string_ = open(sys.argv[1], "rb").read()
  string_ = open("./spc.20160214-000512.polpo.mgz", "rb").read()
  parse_header(string_)
