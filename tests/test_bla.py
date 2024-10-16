import pytest


def test_bla(async_test_app):
    response = async_test_app.get("/health")

    print(response)
