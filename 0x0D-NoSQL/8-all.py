#!/usr/bin/env python3
"""  List all documents in Python """


def list_all(mongo_collection):
    """  List all documents in Python"""
    if not mongo_collection:
        return []
    all_documents = mongo_collection.find()
    return all_documents
