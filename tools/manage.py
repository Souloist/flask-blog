#!/usr/bin/env python

from flask_script import Manager, Server

from app.app import app

manager = Manager(app)
server = Server(host="0.0.0.0", port=5000)

manager.add_command("runserver", server)

if __name__ == "__main__":
    manager.run()
