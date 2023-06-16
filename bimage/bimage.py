"""The bimage module."""

import argparse
import github3
import git



def bimage(gitorg, reponame, branch_or_tag):
        """The bimage function."""

        gh = github3.GitHub()
        repo = gh.repository(gitorg, reponame)
        clone = git.Repo.clone_from(repo.clone_url, reponame)
        clone.git.checkout(branch_or_tag)


if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="Arguments for bimage.")
        parser.add_argument("gitorg", nargs="?")
        parser.add_argument("reponame", nargs="?")
        parser.add_argument("branch_or_tag", nargs="?")
        args = parser.parse_args()
        bimage(args.gitorg, args.reponame, args.branch_or_tag)
