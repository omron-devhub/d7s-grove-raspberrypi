# coding: utf-8
# Driver for D7S.

import smbus
import RPi.GPIO as GPIO
import time

# use the bus that matches your raspi version
rev = GPIO.RPI_REVISION
if rev == 2 or rev == 3:
    bus = smbus.SMBus(1)
else:
    bus = smbus.SMBus(0)

class GroveD7s:
    I2C_ADDR = 0x55

    REG_STATE           = 0x1000
    REG_AXIS_STATE      = 0x1001
    REG_EVENT           = 0x1002
    REG_MODE            = 0x1003
    REG_CTRL            = 0x1004
    REG_CLEAR_COMMAND   = 0x1005
    
    REG_MAIN_SI_H       = 0x2000
    REG_MAIN_SI_L       = 0x2001
    REG_PGA_H           = 0x2002
    REG_PGA_L           = 0x2003

    REG_N1_MAIN_T_AVE_H       = 0x3006
    REG_N1_MAIN_T_AVE_L       = 0x3007
    REG_N1_MAIN_SI_H       = 0x3008
    REG_N1_MAIN_SI_L       = 0x3009
    REG_N1_PGA_H           = 0x300A
    REG_N1_PGA_L           = 0x300B

    REG_N2_MAIN_T_AVE_H       = 0x3006
    REG_N2_MAIN_T_AVE_L       = 0x3007
    REG_N2_MAIN_SI_H       = 0x3008
    REG_N2_MAIN_SI_L       = 0x3009
    REG_N2_PGA_H           = 0x300A
    REG_N2_PGA_L           = 0x300B

    REG_N3_MAIN_T_AVE_H       = 0x3006
    REG_N3_MAIN_T_AVE_L       = 0x3007
    REG_N3_MAIN_SI_H       = 0x3008
    REG_N3_MAIN_SI_L       = 0x3009
    REG_N3_PGA_H           = 0x300A
    REG_N3_PGA_L           = 0x300B

    REG_N4_MAIN_T_AVE_H       = 0x3006
    REG_N4_MAIN_T_AVE_L       = 0x3007
    REG_N4_MAIN_SI_H       = 0x3008
    REG_N4_MAIN_SI_L       = 0x3009
    REG_N4_PGA_H           = 0x300A
    REG_N4_PGA_L           = 0x300B

    REG_N5_MAIN_T_AVE_H       = 0x3006
    REG_N5_MAIN_T_AVE_L       = 0x3007
    REG_N5_MAIN_SI_H       = 0x3008
    REG_N5_MAIN_SI_L       = 0x3009
    REG_N5_PGA_H           = 0x300A
    REG_N5_PGA_L           = 0x300B

    STATUS_NORMAL_MODE                  = 0x00
    STATUS_NORMAL_MODE_NOT_IN_STANBY    = 0x01
    STATUS_INITIAL_INSTALLATION_MODE    = 0x02
    STATUS_OFFSET_ACQUISITION_MODE      = 0x03
    STATUS_SELFTEST_MODE                = 0x04

    def __init__(self):
        self.I2C_ADDR = 0x55
        self.writeByte(self.REG_MODE, 0x02)
        time.sleep(2.0)
        
    def getState(self):
        status = self.readByte(self.REG_STATE)
        return status
    
    def isReady(self):
        try:
            state = self.getState()
            return self.getState() == self.STATUS_NORMAL_MODE
        except OSError:
            print('OSError')
            return False
    
    def isEarthquakeOccuring(self):
        return self.getState() == self.STATUS_NORMAL_MODE_NOT_IN_STANBY

    def getInstantaneusSI(self):
        si = self.readByte16(self.REG_MAIN_SI_H)
        if si != None:
            si /= 10 
        return si

    def getInstantaneusPGA(self):
        pga = self.readByte16(self.REG_PGA_H)
        return pga

    def readByte(self,register16):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        try:
            bus.write_i2c_block_data(self.I2C_ADDR, a1, [a0])
            data = bus.read_byte(self.I2C_ADDR)
            return data
        except OSError:
            return None

    def readByte16(self,register16):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        try:
            bus.write_i2c_block_data(self.I2C_ADDR, a1, [a0])
            data16h = bus.read_byte(self.I2C_ADDR)
            data16l = bus.read_byte(self.I2C_ADDR)
            return (data16h << 8) | (data16l & 0xFF)
        except OSError:
            return None
        
    def writeByte(self,register16, data):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        bus.write_i2c_block_data(self.I2C_ADDR, a1, [a0, (data & 0xFF)])

    def writeByte16(self,register16, data16):
        a1 = (register16 >> 8) & 0xFF
        a0 = register16 & 0xFF
        d1 = (data16 >> 8) & 0xFF
        d0 = data16 & 0xFF
        bus.write_i2c_block_data(self.I2C_ADDR, a1, [a0, d1, d0])
