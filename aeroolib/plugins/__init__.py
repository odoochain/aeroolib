##############################################################################
#
# Copyright (c) 2010 Alistek Ltd. (http://www.alistek.com) All Rights
# Reserved.
#                    General contacts <info@alistek.com>
#
# DISCLAIMER: This module is licensed under GPLv3 or newer and 
# is considered incompatible with OpenERP SA "AGPL + Private Use License"!
#
# Copyright (c) 2007, 2008 OpenHex SPRL. (http://openhex.com) All Rights
# Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

import traceback
import warnings
from io import StringIO

plugins = ['base', 'opendocument']

for name in plugins:
    try:
        __import__('aeroolib.plugins.%s' % name)
    except Exception as e:
        tb_file = StringIO()

        print("Unable to load plugin '%s', you will not be able "
                           "to use it" % name, file=tb_file)
        print("", file=tb_file)
        print('Original traceback:', file=tb_file)
        print('-------------------', file=tb_file)
        traceback.print_exc(file=tb_file)
        print("", file=tb_file)
        warnings.warn(tb_file.getvalue())
