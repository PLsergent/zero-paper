from django.db import models
import unittest
from .models import Folder, Document, Tag

class TestFolder(unittest.TestCase):
    def test_folder_is_instance_of_folder(self): 
        f = Folder(name="foldertest")
        
        self.assertIsInstance(f, Folder) 

    def test_folder_root_is_instance_of_folder(self):
        root = Folder(name="root")
        f = Folder(name="foldertest", parent_folder=root)
        
        self.assertIsInstance(f, Folder)

    def test_str_folder(self):
        f = Folder(name="Testname")
        self.assertEqual(f.__str__(), "Testname")


class TestDocument(unittest.TestCase):
    def test_doc_is_instance_of_document(self):
        doc = Document(title="titletest")
        self.assertIsInstance(doc, Document)

    def test_doctype_is_instance_of_document(self):
        doc = Document(doctype="TXT")
        self.assertIsInstance(doc, Document)

    def test_description_is_instance_of_document(self):
        doc = Document(description="TestText")
        self.assertIsInstance(doc, Document)

    def test_str_document(self):
        doc = Document(title="Testtitle")
        self.assertEqual(doc.__str__(), "Testtitle")

class TestTag(unittest.TestCase):
    def test_tag_is_instance_of_Tag(self):
        tag = Tag(name="TestTag")
        self.assertIsInstance(tag, Tag)
    
    def test_str_tag(self):
        tag = Tag(name="TestTag")
        self.assertEqual(tag.__str__(), "TestTag")