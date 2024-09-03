import logging

from ocs_ci.ocs.ui.base_ui import take_screenshot, copy_dom, BaseUI

logger = logging.getLogger(__name__)


class StorageClients(BaseUI):
    """
    Storage Client page object under PageNavigator / Storage (version 4.14 and above)
    """

    def __init__(self):
        super().__init__()

    def generate_client_onboarding_ticket(self, quota_value=None, quota_tib=None):
        """
        Generate a client onboarding ticket.
        Starting with version 4.17, client quota can be specified

        Args:
            quota_value (int): client's quota in GiB or TiB, unlimited if not defined
            quota_tib (bool): True if quota is in TiB, False otherwise

        Returns:
            str: onboarding_key
        """
        logger.info("Generating onboarding ticket")
        self.do_click(self.storage_clients_loc["generate_client_onboarding_ticket"])
        if quota_value:
            logger.info("Setting client cluster quota")
            self.do_click(self.storage_clients_loc["custom_quota"])
            self.do_clear(
                locator=self.storage_clients_loc["quota_value"],
            )
            self.do_send_keys(
                locator=self.storage_clients_loc["quota_value"],
                text=quota_value,
            )
            if quota_tib:
                self.do_click(self.storage_clients_loc["choose_units"])
                self.do_click(self.storage_clients_loc["quota_ti"])
        logger.info("Confirming token generation")
        self.do_click(self.storage_clients_loc["confirm_generation"])
        onboarding_key = self.get_element_text(
            self.storage_clients_loc["onboarding_key"]
        )
        if len(onboarding_key):
            logger.info("Client onboarding ticket generated")
        else:
            logger.error("Client onboarding ticket generation failed")

        take_screenshot("onboarding_token_modal")
        copy_dom("onboarding_token_modal")

        self.close_onboarding_token_modal()

        return onboarding_key

    def close_onboarding_token_modal(self):
        """
        Close the onboarding token modal
        """
        self.do_click(self.storage_clients_loc["close_token_modal"])
