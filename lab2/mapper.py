#!/usr/bin/env python3

import sys
for line in sys.stdin:
  '''
  .strip() ลบ Whitespace (ช่องว่าง, เว้นวรรค, แท็บ \t, ตัวขึ้นบรรทัดใหม่ \n) ที่อยู่ หัวและท้าย ของข้อความ ออกทั้งหมด
  "  Hello World ".strip() --> "Hello World"

  .split() ตัดแบ่งข้อความออกเป็นคำๆ แล้วเก็บใส่ List
  Hello World".split() --> ['Hello', 'World']
  '''

  for word in line.strip().split():
    if word:
      print(word + "\t1")