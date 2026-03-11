class PullRequest:
    def __init__(self, repository: str, title: str, body: str, head_branch: str):
        self.repository = repository
        self.title = title
        self.body = body
        self.head_branch = head_branch
        self.organization = None
        self.base_branch = None

    def set_organization(self, organization: str):
        self.organization = organization

    def set_base_branch(self, base_branch: str):
        self.base_branch = base_branch
