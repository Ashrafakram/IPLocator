# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:01:04 2023

@author: Dell
"""

import geocoder
import reverse_geocoder as rg

class Iplocator(object):
    def __init__(self, target=geocoder.ip("me")):
        self.data = self.locate(target)
        
    def __str__(self):
        return str(f"\t      [ Ip Locator]\n"
                   f"IP:       {self.data[0]}\n"
                   f"City:     {self.data[1]}\n"
                   f"Country:  {self.data[2]}\n"
                   f"Location: {self.data[3]}")
    
    def locate(self, target):
        latitude, longitude = [*target.latlng]
        city = rg.search((latitude, longitude), verbose=False)
        return [target.ip, city[0]["name"], target.country,[latitude, longitude]]  



if __name__ == "__main__":
    custom_ip = geocoder.ip("1.10.10.0")
    locate = Iplocator(custom_ip)
    print(locate)