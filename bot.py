#!/usr/bin/env python3

import requests
import urllib
import json
import time
import os
from huffman_code import Node, Huffman

TOKEN = os.environ['SECRET_TOKEN']
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

HELP = """
/help
/encode <text>
"""

def make_request(url):
    response = requests.get(url)
    return response


def extract_request_content(response):
    content = response.content.decode("utf8")
    content = json.loads(content)
    return content


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    response = make_request(url)
    print("Update status code: ", response.status_code)
    content = extract_request_content(response)
    return content


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(
          text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    response = make_request(url)
    print("Message send status code: ", response.status_code)


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))

    return max(update_ids)


def extract_useful_info(message):
    if "text" not in message.keys():
        message["text"] = "/start"

    if "first_name" not in message["chat"].keys():
        message["chat"]["first_name"] = "Grupo"

    command = message["text"].split(" ", 1)[0]
    chat = message["chat"]["id"]
    user = message["chat"]["first_name"]

    msg = ''
    if len(message["text"].split(" ", 1)) > 1:
        msg = message["text"].split(" ", 1)[1].strip()

    return command, msg, chat, user


def handle_updates(updates):
    for update in updates["result"]:
        if "message" in update:
            message = update["message"]
        elif "edited_message" in update:
            message = update["edited_message"]
        else:
            print("Can't process! {}".format(update))
            return

        command, msg, chat, user = extract_useful_info(message)

        print(command, msg, chat)

        if command == "/start" or command == "/help":
            send_message("Here is a list of things you can do.", chat)
            send_message(HELP, chat)

        elif command == "/encode":
            try: 
                huffman = Huffman(msg)
                encoded_text_answer = "Text encoded\n\\[" + huffman.encoded_text + "]"
                if(len(encoded_text_answer) > 4096):
                    blocks4096 = [encoded_text_answer[i:i+4096] for i in range(0, len(encoded_text_answer), 4096)]
                    for block4096 in blocks4096:
                        send_message(block4096, chat)
                else:
                    send_message(encoded_text_answer, chat)
                send_message("Text encoded\n\\[" + str(len(huffman.encoded_text)) + " BITS]", chat)
                send_message("Text in ASCII\n\\[" + str(len(huffman.text) * 8) + " BITS]", chat)
                send_message("Text decoded\n\\[" + huffman.decoded_text + "]", chat)
                send_message("Bits saved\n\\[" + str(len(huffman.text) * 8 - len(huffman.encoded_text)) + " BITS]", chat)
                send_message("Characters frequency\n" + str(huffman.characters_frequency), chat)
                send_message("Characters codes\n" + str(huffman.characters_codes), chat)
            except:
                send_message("The command was used wrongly", chat)
        
        else:
            send_message("I'm sorry {}. I'm afraid I can't do that.".format(
                         user), chat)


def main():
    last_update_id = None

    while True:
        print("Updates")
        updates = get_updates(last_update_id)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                handle_updates(updates)
        except:
            print("Update error")

        time.sleep(0.5)


if __name__ == '__main__':

    try:
        main()

    except KeyboardInterrupt:
        print('Interruption')