# -*- coding: utf-8 -*-
from kraeks.plonetraining import _
from Products.Five.browser import BrowserView
from DateTime import DateTime
from plone import api

class Bootstrap(BrowserView):

    def __call__(self):
        self.portaltitle = api.portal.get().title
        today = DateTime()
        self.localized = api.portal.get_localized_time(datetime=today)
        return self.index()
