#!/usr/bin/env python

from __future__ import absolute_import

from app import app

def createdb():
    app.db.create_all()


if __name__ == "__main__":
    createdb()
    app.app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
