from ddfTestCase import ddfTestCase
import unittest

class SetupGeosciencesAustraliaGazetteer2010WebFeatureServerFederatedSource(ddfTestCase):

    def test_setup_geosciences_australia_gazetteer2010_web_feature_server_federated_source(self):
	self.navigate_to_config_page()
        self.click_config_menu_entry("WFS Federated Source")
        self.fill_field("wfsUrl", "http://www.ga.gov.au/gis/services/topography/Gazetteer_2010/MapServer/WFSServer")
        self.click_checkbox("disableSSLCertVerification")
        self.fill_field("id", "GA Gazetter 2010")
        self.click_save()

if __name__ == "__main__":
    unittest.main()
