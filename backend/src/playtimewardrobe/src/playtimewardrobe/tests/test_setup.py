"""Setup tests for this package."""
from playtimewardrobe.testing import PLAYTIMEWARDROBE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer

import unittest


class TestSetup(unittest.TestCase):
    """Test that playtimewardrobe is properly installed."""

    layer = PLAYTIMEWARDROBE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if playtimewardrobe is installed."""
        self.assertTrue(self.installer.is_product_installed("playtimewardrobe"))

    def test_browserlayer(self):
        """Test that IPLAYTIMEWARDROBELayer is registered."""
        from playtimewardrobe.interfaces import IPLAYTIMEWARDROBELayer
        from plone.browserlayer import utils

        self.assertIn(IPLAYTIMEWARDROBELayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("playtimewardrobe:default")[0],
            "20221115001",
        )


class TestUninstall(unittest.TestCase):

    layer = PLAYTIMEWARDROBE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("playtimewardrobe")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if playtimewardrobe is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("playtimewardrobe"))

    def test_browserlayer_removed(self):
        """Test that IPLAYTIMEWARDROBELayer is removed."""
        from playtimewardrobe.interfaces import IPLAYTIMEWARDROBELayer
        from plone.browserlayer import utils

        self.assertNotIn(IPLAYTIMEWARDROBELayer, utils.registered_layers())
