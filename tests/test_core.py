"""Tests for Stylemirror."""
from src.core import Stylemirror
def test_init(): assert Stylemirror().get_stats()["ops"] == 0
def test_op(): c = Stylemirror(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Stylemirror(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Stylemirror(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Stylemirror(); r = c.process(); assert r["service"] == "stylemirror"
