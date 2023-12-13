from datetime import date
import random
from site_passphrase import SitePassphrase
from passphrase_generator import PassphraseGenerator


class SitePassphraseManager:
    def __init__(self, passphrase_generator: PassphraseGenerator, random_generator: random.Random, filename: str=''):
        """
            Initialize a site passphrase manager.
                :param passphrase_generator: The passphrase generator.
                :param random_generator: The random generator.
                :param filename: The filename to load the site passphrases from.
                :returns: None
        """
        pass
    
    def save(self, filename: str) -> None:
        """
            Save the site passphrases to a file.
                :param self: The site passphrase manager object.
                :param filename: The filename to save the site passphrases to.
                :returns: None
        """
        pass

    def add(self, site_name: str, site_url: str, username: str, site_passphrase: str = '') -> None:
        """
            Add a site passphrase.
                :param self: The site passphrase manager object.
                :param site_name: The name of the site.
                :param site_url: The url of the site.
                :param username: The username of the site.
                :param site_passphrase: The passphrase of the site.
                :returns: None  
            """
        pass

    def get_passphrase_for_site(self, site_name: str) -> str:
        """
            Get the passphrase for a site.
                :param self: The site passphrase manager object.
                :param site_name: The name of the site.
                :returns: The passphrase for the site.  
        """
        pass
    
    def refresh_password_for_site(self, site_name: str, new_site_passphrase: str = '') -> None:
        """
            Refresh the passphrase for a site.
                :param self: The site passphrase manager object.
                :param site_name: The name of the site.
                :param new_site_passphrase: The new passphrase for the site.
                :returns: None
        """
        pass
    
    def get_count(self) -> int:
        """
            Get the number of site passphrases.
                :param self: The site passphrase manager object.
                :returns: The number of site passphrases.
        """
        pass
        
    
    
        
