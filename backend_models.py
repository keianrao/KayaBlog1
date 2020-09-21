
from collections import namedtuple

Blogpost = namedtuple('Blogpost', ['title', 'authorUsername', 'submissionDate', 'tags', 'contents'])

BlogpostListing = namedtuple('BlogpostListing', ['id', 'title', 'authorUsername', 'submissionDate', 'tags'])

BlogpostAuthorSearch = namedtuple('BlogpostAuthorSearch', ['author'])

BlogpostTagSearch = namedtuple('BlogpostTagSearch', ['tags'])

BlogpostSubmission = namedtuple('BlogpostSubmission', ['blogpost', 'username', 'password'])

