# coding: utf-8
# Sample to draw graph values acquired with D7S.

from __future__ import print_function

import time
import datetime

import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib import dates as mdates

import grove_d7s

sensor = grove_d7s.GroveD7s()

COLOR_RED = 'tab:red'
COLOR_BLUE = 'tab:blue'

def main():
    if sensor.isReady() == False:
        print('.')
        time.sleep(1.0)
        
    plt.ion()
    fig, ax1 = plt.subplots()
    
    plt.title('D7S Demo')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('SI Value[Kine]', color=COLOR_BLUE)
    ax2 = ax1.twinx()
    ax2.set_ylabel('PGA[gal]', color=COLOR_RED)
    
    oldSi = 0
    oldPga = 0
    siList = []
    pgaList = []
    timeList = []
              
    print ("start")
    
    while True:
          if sensor.isEarthquakeOccuring() == True:
              si = sensor.getInstantaneusSI()
              pga = sensor.getInstantaneusPGA()
              now = datetime.datetime.today()
              
              if si == None or pga == None:
                  continue
                   
              siList.append(si)
              pgaList.append(pga)
              timeList.append(now)
              
              print(now.strftime("[%Y/%m/%d %H:%M:%S]")
                        ,"SI=%.1f[Kine]" %si,"PGA=%d[gal]" %pga)
              
              ax1.plot(timeList, siList, color=COLOR_BLUE)
              ax1.tick_params(axis='y', labelcolor=COLOR_BLUE)
                
              ax2.plot(timeList, pgaList, color=COLOR_RED)
              ax2.tick_params(axis='y', labelcolor=COLOR_RED)

              plt.gcf().autofmt_xdate()
              myFmt = mdates.DateFormatter('%H:%M:%S')
              plt.gca().xaxis.set_major_formatter(myFmt)
                
              fig.tight_layout()
              fig.canvas.draw()
              plt.show()
            
              oldSi = si
              oldPga = pga

if __name__ == '__main__':
  main()
