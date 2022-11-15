from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import playtimewardrobe


class PLAYTIMEWARDROBELayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=playtimewardrobe)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "playtimewardrobe:default")
        applyProfile(portal, "playtimewardrobe:initial")


PLAYTIMEWARDROBE_FIXTURE = PLAYTIMEWARDROBELayer()


PLAYTIMEWARDROBE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLAYTIMEWARDROBE_FIXTURE,),
    name="PLAYTIMEWARDROBELayer:IntegrationTesting",
)


PLAYTIMEWARDROBE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLAYTIMEWARDROBE_FIXTURE, WSGI_SERVER_FIXTURE),
    name="PLAYTIMEWARDROBELayer:FunctionalTesting",
)


PLAYTIMEWARDROBEACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLAYTIMEWARDROBE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="PLAYTIMEWARDROBELayer:AcceptanceTesting",
)
