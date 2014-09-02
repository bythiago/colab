
from django.conf import settings

from ..utils import ColabProxyView


class GitlabProxyView(ColabProxyView):
    upstream = settings.COLAB_GITLAB_URL
    diazo_theme_template = 'proxy/gitlab.html'
