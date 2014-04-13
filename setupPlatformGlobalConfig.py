from ddfTestCase import ddfTestCase
import unittest

from ddfConfigParameters import siteContact, ipAddress, siteIdentifier

class SetupPlatformGlobalConfig(ddfTestCase):

    def test_setup_platform_global_configuration(self):
        self.navigate_to_config_page()
        self.click_config_menu_entry("Platform Global Configuration")
        self.fill_field("host", ipAddress)
        self.fill_field("contact", siteContact)
        self.fill_field("id", siteIdentifier)
        self.click_save()

if __name__ == "__main__":
    unittest.main()
