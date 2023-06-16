"""The bimage module."""


import github3
import git


def bimage(gitorg, reponame, branch_or_tag):
        """The bimage function."""

        gh = github3.GitHub()
        repo = gh.repository(gitorg, reponame)
        clone = git.Repo.clone_from(repo.clone_url, reponame)
        clone.git.checkout(branch_or_tag)
