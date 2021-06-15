#!/usr/bin/env python3
"""nsert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """nsert a document in Python"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
