from FaustBot.Communication import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from cookies import cookies
import random

class GiveCookieObserver(PrivMsgObserverPrototype):
    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.cookie') == -1:
            return
        connection.send_back('\001ACTION schenkt ' 
			     + data['nick'] 
			     + ' einen ' 
			     + random.choice(cookies) 
			     + '.\001', data)
