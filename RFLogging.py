from websocket import create_connection
c = create_connection("ws://radiant-wildwood-39558.herokuapp.com/")

ROBOT_LISTENER_API_VERSION = 2

def start_suite(name, attributes):
    c.send("--- START SUITE '%s' ---" % name)

def end_suite(name, attributes):
    c.send("--- END SUITE '%s' --- %s " % (name, attributes["status"]))

def start_test(name, attributes):
    c.send("--- START TEST '%s' ---" % name)

def end_test(name, attributes):
    c.send("--- END TEST '%s' --- %s " % (name, attributes["status"]))

def start_keyword(name, attributes):
    c.send("--- START KEYWORD '%s' ---" % name)

def end_keyword(name, attributes):
    c.send("--- END KEYWORD '%s' --- %s " % (name, attributes["status"]))

def log_message(message):
    c.send(message["message"])
