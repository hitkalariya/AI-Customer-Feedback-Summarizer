# Customer Feedback Analysis System

A comprehensive Python application designed to analyze and process customer feedback data with advanced sentiment analysis, keyword extraction, and data visualization capabilities.

## Overview

The Customer Feedback Analysis System is a powerful tool that helps businesses understand customer sentiment, identify key themes, and extract actionable insights from customer feedback. The application provides multiple analysis types including sentiment analysis, keyword extraction, topic modeling, and summary generation.

## Features

### Core Analysis Capabilities
- **Sentiment Analysis**: Automatically categorize feedback as positive, negative, or neutral
- **Keyword Extraction**: Identify the most frequently mentioned terms and phrases
- **Topic Modeling**: Group feedback by common themes and topics
- **Summary Generation**: Create comprehensive summaries of feedback data

### Data Visualization
- Interactive charts and graphs using matplotlib
- Pie charts for sentiment distribution
- Bar charts for keyword frequency
- Histograms for feedback length analysis
- Trend analysis over time

### User Interface
- Modern GUI built with tkinter
- File browser for data import
- Real-time analysis results
- Export functionality for reports
- Multi-threaded processing for better performance

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/hitkalariya
   cd customer-feedback-analyzer
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python feedback_analyzer.py
   ```

## Usage

### Getting Started

1. Launch the application by running `feedback_analyzer.py`
2. Click "Browse Files" to select your feedback data file
3. Choose the type of analysis you want to perform:
   - **Sentiment Analysis**: Categorize feedback by sentiment
   - **Keyword Extraction**: Find most common terms
   - **Topic Modeling**: Identify common themes
   - **Summary Generation**: Create comprehensive summaries
4. Click "Start Analysis" to process your data
5. View results in the text area
6. Use "Export Results" to save your analysis

### Supported File Formats

The application supports multiple data formats:
- **CSV files**: Comma-separated values with headers
- **Excel files**: .xlsx format
- **Text files**: One feedback entry per line

### Data Format Requirements

Your data file should contain a column with feedback text. The application will automatically detect columns with names like:
- feedback
- review
- comment
- text
- message
- response

If no obvious column name is found, the first text column will be used.

## Analysis Types

### Sentiment Analysis
Analyzes the emotional tone of feedback using a comprehensive dictionary of positive and negative words. Results include:
- Percentage breakdown of positive, negative, and neutral feedback
- Overall sentiment classification
- Detailed statistics

### Keyword Extraction
Identifies the most frequently mentioned words and phrases in your feedback:
- Removes common stop words
- Counts word frequencies
- Shows top 20 keywords with occurrence counts

### Topic Modeling
Groups feedback by common themes and topics:
- Customer Service
- Product Quality
- Price/Value
- Delivery/Shipping
- Website/App
- Communication

### Summary Generation
Creates comprehensive summaries of feedback data:
- Total feedback count
- Average feedback length
- Most common themes
- Quick sentiment overview

## File Structure

```
customer-feedback-analyzer/
├── feedback_analyzer.py          # Main application entry point
├── feedback_interface.py         # GUI implementation
├── feedback_processor.py         # Core analysis logic
├── data_visualizer.py           # Chart and graph creation
├── sample_feedback.csv          # Example data file
├── requirements.txt             # Python dependencies
└── README.md                   # This documentation
```

## Dependencies

- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization and chart creation
- **numpy**: Numerical computing
- **openpyxl**: Excel file support
- **tkinter**: GUI framework (included with Python)

## Example Output

### Sentiment Analysis Results
```
=== SENTIMENT ANALYSIS RESULTS ===

Total feedback analyzed: 15
Positive feedback: 8 (53.3%)
Negative feedback: 4 (26.7%)
Neutral feedback: 3 (20.0%)

Overall Sentiment: POSITIVE
```

### Keyword Analysis Results
```
=== KEYWORD ANALYSIS RESULTS ===

Top 20 Keywords:
------------------------------
product: 8 occurrences
service: 6 occurrences
quality: 5 occurrences
customer: 4 occurrences
great: 4 occurrences
```

## Contributing

We welcome contributions to improve the Customer Feedback Analysis System. Please feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Create an issue on the GitHub repository
- Check the documentation for common questions
- Review the example data file for format requirements

## Version History

- **v1.0.0**: Initial release with core analysis features
- **v1.1.0**: Added data visualization capabilities
- **v1.2.0**: Enhanced GUI and export functionality

## Acknowledgments

- Built with Python and tkinter
- Data visualization powered by matplotlib
- Data processing with pandas
- Community feedback and testing

---

**Note**: This application is designed for educational and business use. Always ensure you have permission to analyze customer data and comply with relevant privacy regulations.
