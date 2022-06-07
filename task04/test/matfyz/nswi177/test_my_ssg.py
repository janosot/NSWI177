#!/usr/bin/env python

from nose.tools import eq_

from matfyz.nswi177.my_ssg import markdownify, get_html_filename

def test_get_html_filename():
    eq_(get_html_filename("index.md"), "index.html")



