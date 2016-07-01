import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello P!"
line2 = "We can write anything we want here"
line3 = "Use Pythoon"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

