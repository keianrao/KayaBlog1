
from collections import namedtuple

Blogpost = namedtuple('Blogpost', ['author', 'tags', 'contents'])
# About what we choose here. At a minimum we need a contents field, 
# for what's written in the blog post itself. But the other fields
# are metadata, and, if the contents is some sort of markup,
# then maybe it could have the metadata inside of it..
#
# About markup. Based on what I've seen, it seems like it's an
# inherent problem, that a blogger must support some sort of markup
# - and the code they write, or the libraries they depend on,
# are affected by the choice. Now, theoretically we could support 
# only text. But, while that does already allow for many blog posts,
# it's not what I would consider part of a 'good' blogger..
# We're going to headings, links, and images - they're essential for
# interesting blog posts, or long-form documents.
#
# If you decide to support markup, your frontend needs to be
# able to render the markup. And metadata should probably be
# broken out, so that the backend can do things like sorting
# and searching.
#
# Being an app that runs on the modern WWW platform, we know that
# the frontend can dump HTML into the document and the browser will
# render all of it for us (formatting text, highlighting links, etc.).
# And I've read that, it used to be that bloggers did go for HTML
# as their user-submitted markup, since it's very much up for the task,
# and you don't need to expend work processing things much. But
# as time went on, bloggers supported their own markup system -
# see Wikipedia, forums..
# 
# What's normal today might be to say support Markdown, but actually
# I think I'm going to leverage the browser, and just use HTML.
# But I can't just accept, save, load it freely, because I think
# you can inject things that way (inline <script>?). So I think we'll
# define a subset of HTML we're okay with (basically an allowlist of
# HTML tags). Then we'll need clientside or serverside validation that
# boots out anything that isn't within that subset.
#
# What I'm worried about is if we fail to filter.. user submits
# content, it's saved as-is into the database, then loaded back by
# basically "copy-pasting" using .innerHTML.. Whereas if user
# submits markup then when we load it back we actually read through it
# and generate our own HTML, then that's safer since, 
# we're building the HTML. But there's a tradeoff.
#
# ...Anyways, back to the tuple fields. If we do this .innerHTML
# route, then I won't be extracting fields from the content.
# So things that go in different places will be different fields.
# The title, tags, will be in containers by themselves.
