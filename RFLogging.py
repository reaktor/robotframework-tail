import websocket
ws = websocket.WebSocket()
ws.connect("ws://localhost/websocket")

ROBOT_LISTENER_API_VERSION = 2

def start_suite(name, attributes):
    print("--- START SUITE '%s' ---" % name)

def end_suite(name, attributes):
    print("--- END SUITE '%s' ---" % name, attributes["status"])

def start_test(name, attributes):
    print("--- START TEST '%s' ---" % name)

def end_test(name, attributes):
    print("--- END TEST '%s' ---" % name, attributes["status"])

def start_keyword(name, attributes):
    print("--- START KEYWORD '%s' ---" % name)

def end_keyword(name, attributes):
    print("--- END KEYWORD '%s' ---" % name, attributes["status"])

def log_message(message):
    print(message["message"])
