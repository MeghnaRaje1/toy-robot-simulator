import unittest

def run_tests():
    loader = unittest.TestLoader()
    start_dir = 'tests'  
    suite = loader.discover(start_dir)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result

if __name__ == '__main__':
    result = run_tests()
    if result.wasSuccessful():
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
