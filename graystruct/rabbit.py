# -*- coding: utf-8 -*-
# Copyright (c) 2015 Simon Jagoe
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the 3-clause BSD license.  See the LICENSE.txt file for details.
from __future__ import absolute_import
from graypy.rabbitmq import GELFRabbitHandler as BaseGELFRabbitHandler

from .handler import _CompressHandler


class GELFRabbitHandler(_CompressHandler, BaseGELFRabbitHandler):
    pass