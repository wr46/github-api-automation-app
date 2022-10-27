from github import Github

from github_automation.configuration import config


def _get_api() -> Github:
    token = config.GITHUB_TOKEN
    hostname = config.GITHUB_HOSTNAME
    base_url = f'https://{hostname}{config.GITHUB_API_URL_VERSION}'
    return Github(token) if hostname == '' else Github(base_url, token)


api = _get_api()
