from websocket import create_connection
import uuid
import json

c = create_connection("ws://radiant-wildwood-39558.herokuapp.com/")
myid = str(uuid.uuid4())
message_index = 0

c.send(json.dumps([myid, message_index]))
message_index += 1

ROBOT_LISTENER_API_VERSION = 2

def start_suite(name, attributes):
    _send("START", "SUITE '%s'" % name)

def _send(command, data):
    global message_index
    c.send(json.dumps([myid, message_index, command, data]))
    message_index += 1

def end_suite(name, attributes):
    _send("END", "SUITE '%s' -> %s" % (name, attributes["status"]))

def start_test(name, attributes):
    _send("START", "TEST '%s'" % name)

def end_test(name, attributes):
    _send("END", "TEST '%s' => %s " % (name, attributes["status"]))

def start_keyword(name, attributes):
    _send("START", "KEYWORD '%s'" % name)

def end_keyword(name, attributes):
    _send("END", "KEYWORD '%s' => %s " % (name, attributes["status"]))

def log_message(message):
    _send("MESSAGE", message["message"])

def close():
    _send("CLOSE", "CLOSE")
