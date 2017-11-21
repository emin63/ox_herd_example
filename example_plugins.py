"""Example ox_herd plugins used by our app
"""


import requests

# Import base class so we can create plugins
from ox_herd.core.plugins import base


class CheckWeb(base.OxPlugTask):
    """Class to check on a web site.

    This is meanly meant to serve as an example of a minimal plugin.
    All we do is implement the main_call method.
    """

    @classmethod
    def main_call(cls, ox_herd_task):
        """Main method to check if web site is accesible.

        :arg ox_herd_task:   Instance of a CheckWeb task perhaps containing
                        additional data (e.g., ox_herd_task.name). If your
                        main_call does not need arguments, you can basically
                        just ignore ox_herd_task. If you do want to be able
                        to pass in arguments, see a more detailed discussion
                        of how to get arguments from the user and configure
                        a task in the full plugin documentation.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        :returns:       Dictionary with 'return_value' and 'json_blob' as
                        required for OxPluginComponent.

        ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

        PURPOSE:        Check if website is live.

        """
        url = 'http://github.com'
        result = requests.get(url)
        return {
            'return_value': 'Status=%s for checking url %s' % (
                url, result.status_code)
            }
