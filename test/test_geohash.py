import sys

# Test the source tree, not an installed version.
sys.path.insert(0, '../geohash')

import geohash


def test_encode():
    outhash = geohash.encode(42.6, -5.6)
    assert outhash == "ezs42e44yx96"

    outhash = geohash.encode(42.6, -5.6, precision=5)
    assert outhash == "ezs42"
    outhash = geohash.encode(42.6, -5.6, precision=1)


def test_decode():
    lat, lon =  geohash.decode('ezs42')
    assert lat == "42.6"
    assert lon == "-5.6"


def test_decode_exactly():
    lat, lon, lat_err, lon_err = geohash.decode_exactly("ezs42")
    assert lat == 42.60498046875
    assert lon == -5.60302734375
    assert lat_err == 0.02197265625
    assert lon_err == 0.02197265625
