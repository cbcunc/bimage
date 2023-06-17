
Model package for building container images
===========================================

Just modeling some package structure.

To use as a package:

    >>> from bimage import bimage
    >>> bimage.bimage("cbcunc", "timage", "develop")
    >>>

To use as a script:

    usage: bimage [-h] github_org repo_name branch_or_tag

    positional arguments:
        =============  ==============================================
        github_org     The GitHub organization of the repository
        repo_name      The name of the repository in the organization
        branch_or_tag  The branch or tag of the repository
        =============  ==============================================

    options:
        -h, --help     show this help message and exit
