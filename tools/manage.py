#!/usr/bin/env python

from flask_script import Manager, Server

from app import app

manager = Manager(app.app)
server = Server(host="0.0.0.0", port=5000)

manager.add_command("runserver", server)

def createdb():
    app.db.create_all()


if __name__ == "__main__":
    createdb()
    app.app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
