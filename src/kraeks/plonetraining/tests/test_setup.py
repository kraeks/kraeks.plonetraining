# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from kraeks.plonetraining.testing import KRAEKS_PLONETRAINING_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that kraeks.plonetraining is properly installed."""

    layer = KRAEKS_PLONETRAINING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if kraeks.plonetraining is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'kraeks.plonetraining'))

    def test_browserlayer(self):
        """Test that IKraeksPlonetrainingLayer is registered."""
        from kraeks.plonetraining.interfaces import (
            IKraeksPlonetrainingLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IKraeksPlonetrainingLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = KRAEKS_PLONETRAINING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['kraeks.plonetraining'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if kraeks.plonetraining is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'kraeks.plonetraining'))

    def test_browserlayer_removed(self):
        """Test that IKraeksPlonetrainingLayer is removed."""
        from kraeks.plonetraining.interfaces import \
            IKraeksPlonetrainingLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IKraeksPlonetrainingLayer,
            utils.registered_layers())
