#!/usr/bin/env python3
""" Change school topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """ Change school topics"""
    mongo_collection.update(
        {"name": name}, {"$set": {"topics": topics}}, multi=True)
