#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from lcd import lcd

def test_lcd_zero():
    assert_equals(lcd(0), " _ \n| |\n|_|")
    
def test_lcd_one():
    assert_equals(lcd(1), "   \n  |\n  |")

def test_lcd_two():
    assert_equals(lcd(2), " _ \n _|\n|_ ")

def test_lcd_three():
    assert_equals(lcd(3), " _ \n _|\n _|")

def test_lcd_four():
    assert_equals(lcd(4), "   \n|_|\n  |")

def test_lcd_five():
    assert_equals(lcd(5), " _ \n|_ \n _|")
    
def test_lcd_six():
    assert_equals(lcd(6), " _ \n|_ \n|_|")
    
def test_lcd_seven():
    assert_equals(lcd(7), " _ \n  |\n  |")
    
def test_lcd_eight():
    assert_equals(lcd(8), " _ \n|_|\n|_|") 
    
def test_lcd_nine():
    assert_equals(lcd(9), " _ \n|_|\n _|")     
    
def test_lcd_onefourseven():
    assert_equals(lcd(147), """\
       _ 
  ||_|  |
  |  |  |""")
  
def test_lcd_all():
    assert_equals(lcd(123456789), """\
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|""")
  
def test_lcd_string():
    assert_equals(lcd("0123456789"), """\
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|""")
