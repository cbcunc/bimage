
Model package for building container images
===========================================

Just modeling some package structure.

To use as a package:

    >>> from bimage import bimage
    >>> bimage.bimage("cbcunc", "timage", "develop")
    >>>

To use as a script:
   usage: bimage.py [-h] [gitorg] [reponame] [branch_or_tag]

   Arguments for bimage.

   positional arguments:
     gitorg
     reponame
     branch_or_tag

   options:
     -h, --help     show this help message and exit
