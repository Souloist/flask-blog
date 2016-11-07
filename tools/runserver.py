#!/usr/bin/env python

from __future__ import absolute_import

from blog.app import app
from blog.models.meta import Base, engine
import blog.models.user

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
