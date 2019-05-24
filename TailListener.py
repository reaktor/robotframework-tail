#  Copyright 2019 Reaktor
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from websocket import create_connection
import uuid
import json

c = create_connection("ws://localhost:3000/")
myid = str(uuid.uuid4())
message_index = 0

c.send(json.dumps([myid, message_index]))
message_index += 1

ROBOT_LISTENER_API_VERSION = 2

def start_suite(name, attributes):
    _send("START", "SUITE", name)

def _send(command, item, data):
    global message_index
    c.send(json.dumps([myid, message_index, command, item, data]))
    message_index += 1

def end_suite(name, attributes):
    _send("END", "SUITE", "'%s' -> %s" % (name, attributes["status"]))

def start_test(name, attributes):
    _send("START", "TEST",  name)

def end_test(name, attributes):
    _send("END", "TEST", "'%s' => %s " % (name, attributes["status"]))

def start_keyword(name, attributes):
    _send("START", "KEYWORD", name)

def end_keyword(name, attributes):
    _send("END", "KEYWORD", "'%s' => %s " % (name, attributes["status"]))

def log_message(message):
    _send("MESSAGE", "MESSAGE", message["message"])

def close():
    _send("CLOSE", "CLOSE", "CLOSE")
