# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE
    PloneSandboxLayer,
)
from plone.testing import z2

import kraeks.plonetraining


class KraeksPlonetrainingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=kraeks.plonetraining)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'kraeks.plonetraining:default')


KRAEKS_PLONETRAINING_FIXTURE = KraeksPlonetrainingLayer()


KRAEKS_PLONETRAINING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(KRAEKS_PLONETRAINING_FIXTURE,),
    name='KraeksPlonetrainingLayer:IntegrationTesting',
)


KRAEKS_PLONETRAINING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(KRAEKS_PLONETRAINING_FIXTURE,),
    name='KraeksPlonetrainingLayer:FunctionalTesting',
)


KRAEKS_PLONETRAINING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        KRAEKS_PLONETRAINING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='KraeksPlonetrainingLayer:AcceptanceTesting',
)
