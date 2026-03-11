from github import Auth, Github

from github_automation.configuration import config


_PUBLIC_GITHUB_DOMAINS = ('', 'github.com', 'www.github.com', 'api.github.com')


def _is_public_github(hostname: str) -> bool:
    return not hostname or any(
        hostname == h or hostname.startswith(h + '/') for h in _PUBLIC_GITHUB_DOMAINS
    )


def _get_api() -> Github:
    token = config.GITHUB_TOKEN
    hostname = config.GITHUB_HOSTNAME
    auth = Auth.Token(token) if token else None
    if _is_public_github(hostname):
        return Github(auth=auth)
    base_url = f'https://{hostname}{config.GITHUB_API_URL_VERSION}'
    return Github(auth=auth, base_url=base_url)


api = _get_api()
