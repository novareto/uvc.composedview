# -*- coding: utf-8 -*-

import zope.security

from collections import OrderedDict
from operator import itemgetter

from dolmen.field import GlobalClass
from grokcore.chameleon.components import ChameleonPageTemplateFile
from grokcore.component import baseclass, title, sort_components
from megrok.layout import Page
from zope.component import getAdapters
from zope.interface import implementer, Interface
from zope.publisher.interfaces.browser import IBrowserPage
from zope.schema import Dict, TextLine


def check_security(component, attribute):
    try:
        return zope.security.canAccess(component, attribute)
    except zope.security.interfaces.Forbidden:
        return False


class ITab(IBrowserPage):
    pass


class IComposedRenderable(Interface):

    title = TextLine(
        title=u"Title of the page",
        required=True,
        )

    tabs = Dict(
        title=u"Content of the composition",
        required=True,
        value_type=GlobalClass(
            title=u'a class field',
            schema=ITab),
        )

    def details(name):
        """Returns a dict-like object with the detail of a tab.
        """

    def summary():
        """Returns an iterable of details.
        """

    def tab_url(name):
        """Returns the URL of a tab.
        """


def get_tabs(view, update=True):
    tabs = OrderedDict()
    views = sort_components(
        getAdapters((view, view.request), Interface), key=itemgetter(1))
    for id, tab in views:
        if ITab.providedBy(tab):
            # This security check is crap
            # It's due to Grok protecting only __call__
            # This works as long as we don't have a security proxy.
            if check_security(tab, '__call__'):
                if update is True:
                    tab.update()
                tabs[id] = tab
    return tabs


@implementer(IComposedRenderable)
class ComposedPage(Page):
    baseclass()

    tabs = {}
    updating = True
    template = ChameleonPageTemplateFile('composed.cpt')

    @property
    def title(self):
        return title.bind(default=u"").get(self)

    def publishTraverse(self, request, name):
        self.tabs = get_tabs(self, update=False)
        view = self.tabs.get(name)
        if view is not None:
            return view
        return None

    def update(self):
        self.tabs = get_tabs(self, update=True)

    def details(self, id):
        tab = self.tabs.get(id)
        if tab is not None:
            return {
                'title': title.bind(default=id).get(tab),
                'name': id,
                }
        return None

    def summary(self):
        for id in self.tabs:
            yield self.details(id)

    def tab_url(self, id):
        """Returns the URL of a tab.
        """
        return self.url(self, name=id)
