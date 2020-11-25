#!/usr/bin/env python3
import vk_api
import  vk_api.bot_longpoll
from _identifire import group_id, group_token
import random


class Bot:
    def __init__(self, grp_id, grp_token):
        self.grp_id = grp_id
        self.grp_token = grp_token
        self.vk_session = vk_api.VkApi(token=grp_token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk_session, self.grp_id)
        self.vk = self.vk_session.get_api()

    def run(self):
        for event in self.long_poller.listen():
            self.on_event(event)# Listen longpoll

    def on_event(self, event):
        if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            if event.from_user:
                self.message_on_event(event)
            elif event.from_group:
                self.message_on_event(event)
            elif event.from_chat:
                self.message_on_event(event)
            elif event.from_me:
                self.message_on_event(event)
        else:
            print("Can't handle this {} event yet.".format(event.type))

    def message_on_event(self, event):
        self.vk.messages.send(  # Отправляем сообщение
            peer_id = event.object.peer_id,
            random_id = random.randint(0, 2**20),
            message = event.object.text
        )


if __name__ == '__main__':
    vk_bot = Bot(group_id, group_token)
    vk_bot.run()
