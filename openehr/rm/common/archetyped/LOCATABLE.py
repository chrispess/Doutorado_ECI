# -*- coding: utf-8 -*-
__author__ = 'chrispess'


from openehr.rm.common.archetyped.PATHABLE import PATHABLE
from openehr.rm.support.identification.UID_BASED_ID import UID_BASED_ID


class LOCATABLE(PATHABLE):


    uid = UID_BASED_ID
