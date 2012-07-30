from zope.interface import Interface

class IRecipientsResolver(Interface):
    """ An adapter for recipient resolving 
        
        Create your own adapter implementing this interface
    """
    
    def recipients():
        """ Returns list of emails the mail is send to """