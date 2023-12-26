# Describe this function...
def Tello_Get_Barometer__cm_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[11].split(':')[-1]

# Describe this function...
def Tello_Get_Lowest_Temp__Deg_C_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[6].split(':')[-1]

# Describe this function...
def Tello_Get_Motor_Time():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[12].split(':')[-1]

# Describe this function...
def Tello_Get_Pitch__Deg_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[0].split(':')[-1]

# Describe this function...
def Tello_Get_Highest__Deg_C_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[7].split(':')[-1]

# Describe this function...
def Tello_Get_X_Acceleration():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[13].split(':')[-1]

# Describe this function...
def Tello_Get_Yaw__Deg_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[1].split(':')[-1]

# Describe this function...
def Tello_Get_TOF__cm_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[8].split(':')[-1]

# Describe this function...
def Tello_Get_Y_Acceleration():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[14].split(':')[-1]

# Describe this function...
def Tello_Get_Roll__Deg_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[2].split(':')[-1]

# Describe this function...
def Tello_Get_Height__cm_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[9].split(':')[-1]

# Describe this function...
def Tello_Get_Z_Acceleration():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[15].split(':')[-1]

# Describe this function...
def Tello_Get_X_Speed():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[3].split(':')[-1]

# Describe this function...
def Tello_Get_Battery___25_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[10].split(':')[-1]

# Describe this function...
def Tello_Get_Y_Speed():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[4].split(':')[-1]

# Describe this function...
def Tello_Get_Z_Speed():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  return TelloState[5].split(':')[-1]

# Describe this function...
def Tello_Update_State():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState

  udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udpsocket.bind(('0.0.0.0', 8890))
  TSPrev = str(udpsocket.recv(1024).decode())
  TelloState = TSPrev.split(';')
  wait(0.02)

# Describe this function...
def Tello_Connect(Tello_SSID, Tello_Password):
  global cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  wifiCfg.doConnect(Tello_SSID, Tello_Password)

# Describe this function...
def Tello_Init_SDK():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState

  udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udpsocket.connect(('192.168.10.1', 8889))
  udpsocket.sendto('command', ('192.168.10.1', 8889))
  udpsocket.sendto('streamoff', ('192.168.10.1', 8889))

# Describe this function...
def Tello_Takeoff():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto('takeoff', ('192.168.10.1', 8889))

# Describe this function...
def Tello_Land():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto('land', ('192.168.10.1', 8889))

# Describe this function...
def Tello_Emergency_Stop():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto('emergency', ('192.168.10.1', 8889))

# Describe this function...
def Tello_Up(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('up ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Down(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('down ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Left(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('left ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Right(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('right ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Forward(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('forward ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Back(cm):
  global Tello_SSID, Tello_Password, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('back ') + str(cm)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Rotate_Clockwise(deg):
  global Tello_SSID, Tello_Password, cm, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('cw ') + str(deg)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Rotate_Counterclockwise(deg):
  global Tello_SSID, Tello_Password, cm, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('ccw ') + str(deg)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Flip(dir2):
  global Tello_SSID, Tello_Password, cm, deg, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('flip ') + str(dir2)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Set_Speed(Speed):
  global Tello_SSID, Tello_Password, cm, deg, dir2, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('speed ') + str(Speed)), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Fly_to(x, Y, Z, Speed):
  global Tello_SSID, Tello_Password, cm, deg, dir2, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('go ') + str(((str(x) + str(((str(' ') + str(((str(Y) + str(((str(' ') + str(((str(Z) + str(((str(' ') + str(Speed)))))))))))))))))))), ('192.168.10.1', 8889))

# Describe this function...
def Tello_Keepalive__Run_in_loop_every__3C15s_():
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, a, b, c, d, TSPrev, TelloState
  Tello_Update_State()
  udpsocket.sendto('battery?', ('192.168.10.1', 8889))

# Describe this function...
def Tello_Curve(X1, Y1, Z1, X2, Y2, Z2, Speed):
  global Tello_SSID, Tello_Password, cm, deg, dir2, x, Y, Z, a, b, c, d, TSPrev, TelloState
  udpsocket.sendto((str('curve ') + str(((str(X1) + str(((str(' ') + str(((str(Y1) + str(((str(' ') + str(((str(Z1) + str(((str(' ') + str(((str(X2) + str(((str(' ') + str(((str(Y2) + str(((str(' ') + str(((str(Z2) + str(((str(' ') + str(Speed)))))))))))))))))))))))))))))))))))))), ('192.168.10.1', 8889))

# Describe this function...
def Tello_RC_Control(a, b, c, d):
  global Tello_SSID, Tello_Password, cm, deg, dir2, Speed, x, Y, Z, X1, Y1, Z1, X2, Y2, Z2, TSPrev, TelloState
  udpsocket.sendto((str('rc ') + str(((str(a) + str(((str(' ') + str(((str(b) + str(((str(' ') + str(((str(c) + str(((str(' ') + str(d)))))))))))))))))))), ('192.168.10.1', 8889))
