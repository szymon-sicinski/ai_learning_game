# simple test class  to test pytest
class TestExample:
    def test_always_passes(self):
        assert 1 + 1 == 2

    # sample test that will fail
    def test_always_fails(self):
        assert 1 + 2 == 3
