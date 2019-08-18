from sense_hat import SenseHat 
import time
s = SenseHat() 
s.low_light = True
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0) 
pink = (255,105, 180) 
 
 
 
def fantasma(): 
  R = white
  O = nothing
  logo = [
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo 
 
def interactive(): 
  R = green
  O = nothing
  logo = [
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo 
 


def ectoplasm(): 
  R = blue
  O = nothing
  logo = [
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo 
 
def poltergeist(): 
  R = pink
  O = nothing
  logo = [
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo 

def orbs(): 
  R = red
  O = nothing
  logo = [
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo 

def funnel(): 
  R = yellow 
  O = nothing 
  logo = [ 
O, O, O, R, R, O, O, O, 
O, O, R, R, R, R, O, O, 
O, O, R, R, R, R, O, O, 
O, R, O, R, R, O, R, O, 
O, R, O, R, R, O, R, O, 
O, R, R, R, R, R, R, O, 
O, R, R, R, R, R, R, O, 
O, R, O, R, R, O, R, O, 
] 
  return logo

x = fantasma
x1 = interactive
x2 = ectoplasm
x3 = poltergeist
x4 = orbs
x5 = funnel

while True: 
  msg = " searching " 
 
  t = s.get_temperature() 
  
  t = round(t, 1) 
  
  p = s.get_pressure() 
  
  h = s.get_humidity() 
  
  msg1 = "fantasma" 
  
  msg2 = "interactive" 
  
  msg3 = "ectoplasm" 
  
  msg4 = "poltergeist" 
  
  msg5 = "orbs" 
  
  msg6 = "funnel" 
  
  if (t >= -40 and t <= 32) and (p >=260 and p <= 450) and (h > 0 and h <20):
      s.set_pixels(x())
      time.sleep(1.75)
      s.show_message(msg1 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  elif (t >= 32 and t <= 65) and (p >=450 and p <= 600) and (h > 21 and h <40): 
      s.set_pixels(x2())
      time.sleep(1.75) 
      s.show_message(msg2 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  elif (t >= 65 and t <= 80) and (p >=600 and p <= 800) and (h > 40 and h <60):
      s.set_pixels(x1())
      time.sleep(1.75) 
      s.show_message(msg3 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  elif (t >= 80 and t <= 85) and (p >=800 and p <= 1000) and (h > 60 and h <80):
      s.set_pixels(x3())
      time.sleep(1.75) 
      s.show_message(msg4 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  elif (t >= 85 and t <= 105) and (p >=1000 and p <= 1100) and (h > 80 and h <90):
      s.set_pixels(x4())
      time.sleep(1.75) 
      s.show_message(msg5 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  elif (t >= 105 and t <= 120) and (p >=1100 and p <= 1260) and (h > 90 and h <100):
      s.set_pixels(x5())
      time.sleep(1.75)
      s.show_message(msg6 , scroll_speed=0.05, back_colour = nothing)
      time.sleep(0.75)
  else: 
    s.show_message(msg, scroll_speed=0.05, back_colour = nothing) 
