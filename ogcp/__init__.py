# Copyright (C) 2020-2021 Soleta Networks <info@soleta.eu>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.

from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from flask import Flask
from os import urandom

app = Flask(__name__)
app.config.from_json('cfg/ogcp.json')
app.secret_key = urandom(16)

babel = Babel(app)
csrf = CSRFProtect(app)
bootstrap = Bootstrap(app)


import ogcp.views
