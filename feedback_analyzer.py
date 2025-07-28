#!/usr/bin/env python3
"""
Feedback Analysis System - Main Entry Point
A comprehensive tool for analyzing and processing customer feedback data
"""

from feedback_interface import FeedbackAnalyzerInterface

def main():
    """
    Main function to initialize and run the feedback analysis system
    """
    try:
        analyzer = FeedbackAnalyzerInterface()
        analyzer.start_application()
    except Exception as e:
        print(f"Application startup error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 