#!/usr/bin/env python3
"""
Feedback Analysis System - Main Entry Point
A comprehensive tool for analyzing and processing customer feedback data
"""

from feedback_interface import FeedbackAnalyzerInterface
import argparse

def main():
    """
    Main function to initialize and run the feedback analysis system.
    Supports headless mode for batch processing via command-line arguments.
    """
    parser = argparse.ArgumentParser(description="Customer Feedback Analysis System")
    parser.add_argument('--headless', action='store_true', help='Run in headless (no-GUI) mode for batch processing')
    parser.add_argument('--file', type=str, help='Path to feedback data file')
    parser.add_argument('--type', type=str, choices=['sentiment', 'keywords', 'topics', 'summary'], help='Type of analysis to perform')
    args = parser.parse_args()
    if args.headless and args.file and args.type:
        from feedback_processor import FeedbackProcessor
        processor = FeedbackProcessor()
        result = processor.analyze_feedback(args.file, args.type)
        print(result)
        return 0
    try:
        analyzer = FeedbackAnalyzerInterface()
        analyzer.start_application()
    except Exception as e:
        print(f"Application startup error: {e}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main()) 