"""
Copyright (C) 2008 Leonard Norrgard <leonard.norrgard@gmail.com>
Copyright (C) 2015 Leonard Norrgard <leonard.norrgard@gmail.com>

This file is part of geohash.

geohash is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

geohash is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public
License along with geohash.  If not, see
<http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages
setup(
    name = "geohash",
    version = "1.0",
    packages = find_packages(),

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst']
    },

    # metadata for upload to PyPI
    author = "Leonard Norrgard",
    author_email = "leonard.norrgard@gmail.com",
    description = "Module to decode/encode Geohashes to/from latitude and longitude.  See http://en.wikipedia.org/wiki/Geohash",
    long_description = "This module provides functions to decode and encode Geohashes to and from latitude and longitude coordinates.",
    license = "GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.",
    keywords = "Geohash GIS latitude longitude encode decode Galileo GPS WGS84 coordinates geotagging",
    url = "https://github.com/destination-earth-digital-twins/geohash",
)
