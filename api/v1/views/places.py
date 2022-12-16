#!/usr/bin/python3
"""
Module for places views
"""
from api.v1.views import app_views
from models import storage
from models.place import Place
from flask import abort, jsonify, make_response, request



