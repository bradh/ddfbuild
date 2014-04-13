from ddfTestCase import ddfTestCase
import unittest

class SetupOpenSearch(ddfTestCase):

    def test_setup_open_search(self):
	self.navigate_to_config_page()
        self.click_config_menu_entry("OpenSearch Description Document Configuration")
        self.click_checkbox("osddEnabled")
        self.click_save()

if __name__ == "__main__":
    unittest.main()
