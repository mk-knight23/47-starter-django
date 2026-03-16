"""
Example Test Suite
Basic tests to demonstrate pytest usage
"""

def test_basic_assertion():
    """Test basic math operations"""
    assert 1 + 1 == 2

def test_string_operations():
    """Test string handling"""
    text = "hello world"
    assert text.startswith("hello")
    assert "world" in text

def test_list_operations():
    """Test list operations"""
    items = [1, 2, 3, 4, 5]
    assert len(items) == 5
    assert 3 in items

class TestExampleClass:
    """Example test class"""
    
    def test_method(self):
        """Test method in class"""
        assert True is True
