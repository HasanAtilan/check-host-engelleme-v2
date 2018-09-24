""" 
@ Created : MR.HASAN @ SOFTWARE DEVELOPER
@ hasanatilan.com
@ Skype: SkyTime1234
@
"""

import isletimsistemi
isletimsistemi.sistem('iptables -A INPUT -s 31.148.219.0/24 -j DROP')
print "Başarıyla Engellendi"
