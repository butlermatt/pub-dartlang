# Copyright (c) 2012, the Dart project authors.  Please see the AUTHORS file
# for details. All rights reserved. Use of this source code is governed by a
# BSD-style license that can be found in the LICENSE file.

from google.appengine.ext import db

from testcase import TestCase
from models.pubspec import Pubspec

class PubspecTest(TestCase):
    def test_disallows_author_and_authors(self):
        self.assert_invalid_pubspec(author="Bob", authors="Nathan")

    def test_requires_author_to_be_string(self):
        self.assert_invalid_pubspec(author=["Bob"])

    def test_requires_authors_to_be_string_or_list(self):
        self.assert_invalid_pubspec(author=12)

    def test_author(self):
        self.assertEqual(Pubspec(author="Nathan").authors, [("Nathan", None)])

    def test_author_with_email(self):
        self.assertEqual(Pubspec(author="Nathan <nweiz@google.com>").authors,
                         [("Nathan", "nweiz@google.com")])

    def test_empty_string_author(self):
        self.assertEqual(Pubspec(author="").authors, [("", None)])

    def test_weird_author_format(self):
        self.assertEqual(Pubspec(author="Nathan <nweiz").authors,
                         [("Nathan <nweiz", None)])

    def test_single_author_for_authors(self):
        self.assertEqual(Pubspec(authors="Nathan").authors, [("Nathan", None)])

    def test_authors(self):
        self.assertEqual(Pubspec(authors=["Nathan", "Bob"]).authors,
                         [("Nathan", None), ("Bob", None)])

    def test_requires_name_to_be_string(self):
        self.assert_invalid_pubspec(name=12)

    def test_requires_version_to_be_string(self):
        self.assert_invalid_pubspec(version=12)

    def test_requires_homepage_to_be_string(self):
        self.assert_invalid_pubspec(homepage=12)

    def assert_invalid_pubspec(self, **kwargs):
        self.assertRaises(db.BadValueError, lambda: Pubspec(**kwargs))
        
