#!/usr/bin/env python3
"""
Test script to verify WebWarden installation and basic functionality.
"""

import subprocess
import sys
import os

def test_imports():
    """Test that all required modules can be imported."""
    try:
        import playwright
        import bs4
        from rich.console import Console
        print("[PASS] All imports successful")
        return True
    except ImportError as e:
        print(f"[FAIL] Import error: {e}")
        return False

def test_playwright_installation():
    """Test that Playwright browsers are installed."""
    try:
        # Try to run a simple playwright command
        result = subprocess.run([
            sys.executable, "-m", "playwright", "install", "--help"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("[PASS] Playwright is installed correctly")
            return True
        else:
            print("[FAIL] Playwright installation issue")
            return False
    except subprocess.TimeoutExpired:
        print("[FAIL] Playwright test timed out")
        return False
    except Exception as e:
        print(f"[FAIL] Playwright test error: {e}")
        return False

def test_webwarden_help():
    """Test that WebWarden CLI help works."""
    try:
        # Get the directory of this test script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        webwarden_path = os.path.join(script_dir, "webwarden.py")
        
        result = subprocess.run([
            sys.executable, webwarden_path, "--help"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and "WebWarden" in result.stdout:
            print("[PASS] WebWarden CLI is working")
            return True
        else:
            print("[FAIL] WebWarden CLI issue")
            print(f"stdout: {result.stdout}")
            print(f"stderr: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("[FAIL] WebWarden CLI test timed out")
        return False
    except Exception as e:
        print(f"[FAIL] WebWarden CLI test error: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing WebWarden installation...\\n")
    
    tests = [
        test_imports,
        test_playwright_installation,
        test_webwarden_help,
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
        print()  # Add spacing between tests
    
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("\\n[SUCCESS] All tests passed! WebWarden is ready to use.")
        return 0
    else:
        print("\\n[FAILURE] Some tests failed. Please check the installation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())