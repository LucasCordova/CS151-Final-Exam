class SitePassphrase:
    """Class to represent a site passphrase."""
    def __init__(self, site_name: str, site_url: str, username: str, passphrase: str):
        """
            Initialize a site passphrase.
                :param site_name: The name of the site.
                :param site_url: The url of the site.
                :param username: The username of the site.
                :param passphrase: The passphrase of the site. 
                :returns: None
        """
        pass

    def get_site_name(self) -> str:
        """
            Get the site name.
                :param self: The site passphrase object.
                :returns: The site name.
        """
        pass
    
    def get_site_url(self) -> str:
        """
            Get the site url.
                :param self: The site passphrase object.
                :returns: The site url.
        """
        pass
    
    def get_passphrase(self) -> str:
        """
            Get the site passphrase.
            
                :param self: The site passphrase object.
                :returns: The site passphrase.    
        """
        pass
    
    def get_username(self) -> str:
        """
            Get the site username.
                :param self: The site passphrase object.
                :returns: The site username.
        """
        pass
    
    def set_site_name(self, new_site_name: str):
        """
            Set the site name.
                :param self: The site passphrase object.
                :param new_site_name: The new site name.
                :returns: None  
        """
        pass

    def set_site_url(self, new_site_url: str):
        """
            Set the site url.
                :param self: The site passphrase object.
                :param new_site_url: The new site url.
                :returns: None  
        """
        pass
    
    def set_username(self, new_username: str):
        """
            Set the site username.
                :param self: The site passphrase object.
                :param new_username: The new site username.
                :returns: None  
        """
        pass
    
    def set_passphrase(self, new_passphrase: str):
        """
            Set the site passphrase.
                :param self: The site passphrase object.
                :param new_passphrase: The new site passphrase.
                :returns: None  
        """
        pass

    def __str__(self):
        """
            String representation of the site passphrase.
                :param self: The site passphrase object.
                :returns: The string representation of the site passphrase. 
        """
        return f'{self._site_name}|{self._site_url}|{self._username}|{self._passphrase}'
    
    def __repr__(self):
        """
            String representation of the site passphrase.
                :param self: The site passphrase object.
                :returns: The string representation of the site passphrase.
            """
        return self.__str__()

    