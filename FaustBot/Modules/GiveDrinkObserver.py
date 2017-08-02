from FaustBot.Communication.Connection import Connection
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype
from getraenke import getraenke, getraenke_after_work
import random, datetime


class GiveDrinkObserver(PrivMsgObserverPrototype):

    def update_on_priv_msg(self, data: dict, connection: Connection):
        if data['message'].find('.drink') == -1:
            return

        now = datetime.datetime.now()

        if ((now.hour + 2 ) >= 22) or ((now.hour + 2) < 5): #alternativ nur am Wochenende oder sowas
            print('afterwork')
            connection.send_back('\001ACTION schenkt ' + data['nick'] + ' ' + random.choice(getraenke + getraenke_after_work) + ' ein.\001', data)
        else:
            print('work')
            connection.send_back('\001ACTION schenkt ' + data['nick'] + ' ' + random.choice(getraenke) + ' ein.\001', data)
