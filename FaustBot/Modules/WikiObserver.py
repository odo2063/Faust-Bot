from wikipedia import wikipedia

from FaustBot.Model.i18n import i18n
from FaustBot.Modules.PrivMsgObserverPrototype import PrivMsgObserverPrototype


class WikiObserver(PrivMsgObserverPrototype):
    def update_on_priv_msg(self, data, connection):

        if data['message'].find('.w ') == -1:
            return
        i18n_server = i18n()
        w = wikipedia.set_lang(i18n_server.get_text('wiki_lang', lang=self.config.lang))
        q = data['message'].split(' ')
        query = ''
        for word in q:
            if word.strip() != '.w':
                query += word + ' '
        w = wikipedia.search(query)
        if len(w) == 0:  # TODO BUG BELOW, ERROR MESSAGE NOT SHOWN!
            connection.send_back(data['nick'] + ', ' +
                                 i18n_server.get_text('wiki_fail',
                                                      lang=self.config.lang),
                                 data)
            return
        try:
            page = wikipedia.WikipediaPage(w.pop(0))
        except wikipedia.DisambiguationError as error:
            print('disambiguation page')
            page = wikipedia.WikipediaPage(error.args[1][0])
        connection.send_back(data['nick'] + ' ' + page.url, data)
        
        if len(page.summary) < 230:
            connection.send_back(page.summary, data)
        else:
            index = page.summary[0:230].rfind('. ')
            if index == -1:
                index = page.summary[0:230].rfind(' ')
                connection.send_back(page.summary[0:index], data)
            else:
            connection.send_back(page.summary[0:index], data)
