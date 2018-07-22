from nameko.extensions import DependencyProvider
from mailgun_api import MailgunApi
import requests

class MailgunWebservice(DependencyProvider):

    def setup(self):
        self.session = requests.Session()

    def get_dependency(self, worker_ctx):
        return MailgunApi(self.session)
