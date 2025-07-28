"""
Feedback Processing Module
Handles the core logic for analyzing customer feedback data
"""

import pandas as pd
import re
from collections import Counter
import json
from datetime import datetime

class FeedbackProcessor:
    """
    Main class for processing and analyzing customer feedback
    """
    
    def __init__(self):
        self.supported_formats = ['.csv', '.txt', '.xlsx']
        self.positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
            'outstanding', 'perfect', 'love', 'like', 'enjoy', 'satisfied',
            'happy', 'pleased', 'impressed', 'recommend', 'best', 'awesome'
        }
        self.negative_words = {
            'bad', 'terrible', 'awful', 'horrible', 'disappointed', 'frustrated',
            'angry', 'upset', 'hate', 'dislike', 'poor', 'worst', 'useless',
            'broken', 'defective', 'slow', 'expensive', 'difficult', 'confusing'
        }
        
    def analyze_feedback(self, file_path, analysis_type):
        """
        Main method to analyze feedback based on the specified type
        
        Args:
            file_path (str): Path to the feedback data file
            analysis_type (str): Type of analysis to perform
            
        Returns:
            str: Formatted analysis results
        """
        try:
            # Load and validate data
            data = self.load_data(file_path)
            if data is None or data.empty:
                return "Error: No valid data found in the file."
                
            # Perform analysis based on type
            if analysis_type == "sentiment":
                return self.perform_sentiment_analysis(data)
            elif analysis_type == "keywords":
                return self.extract_keywords(data)
            elif analysis_type == "topics":
                return self.identify_topics(data)
            elif analysis_type == "summary":
                return self.generate_summary(data)
            else:
                return "Error: Unknown analysis type."
                
        except Exception as e:
            return f"Analysis error: {str(e)}"
            
    def load_data(self, file_path):
        """
        Load data from various file formats
        
        Args:
            file_path (str): Path to the data file
            
        Returns:
            pandas.DataFrame: Loaded data
        """
        try:
            file_extension = file_path.lower().split('.')[-1]
            
            if file_extension == 'csv':
                return pd.read_csv(file_path, encoding='utf-8')
            elif file_extension == 'xlsx':
                return pd.read_excel(file_path)
            elif file_extension == 'txt':
                # For text files, assume one feedback per line
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                return pd.DataFrame({'feedback': [line.strip() for line in lines if line.strip()]})
            else:
                raise ValueError(f"Unsupported file format: {file_extension}")
                
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
            
    def perform_sentiment_analysis(self, data):
        """
        Perform sentiment analysis on feedback data
        
        Args:
            data (pandas.DataFrame): Feedback data
            
        Returns:
            str: Sentiment analysis results
        """
        results = []
        results.append("=== SENTIMENT ANALYSIS RESULTS ===\n")
        
        # Determine the feedback column
        feedback_col = self.get_feedback_column(data)
        if feedback_col is None:
            return "Error: Could not identify feedback column in data."
            
        positive_count = 0
        negative_count = 0
        neutral_count = 0
        total_feedback = 0
        
        for _, row in data.iterrows():
            feedback_text = str(row[feedback_col]).lower()
            total_feedback += 1
            
            # Count positive and negative words
            positive_words_found = sum(1 for word in self.positive_words if word in feedback_text)
            negative_words_found = sum(1 for word in self.negative_words if word in feedback_text)
            
            if positive_words_found > negative_words_found:
                positive_count += 1
            elif negative_words_found > positive_words_found:
                negative_count += 1
            else:
                neutral_count += 1
                
        # Calculate percentages
        total = len(data)
        positive_pct = (positive_count / total) * 100 if total > 0 else 0
        negative_pct = (negative_count / total) * 100 if total > 0 else 0
        neutral_pct = (neutral_count / total) * 100 if total > 0 else 0
        
        results.append(f"Total feedback analyzed: {total}")
        results.append(f"Positive feedback: {positive_count} ({positive_pct:.1f}%)")
        results.append(f"Negative feedback: {negative_count} ({negative_pct:.1f}%)")
        results.append(f"Neutral feedback: {neutral_count} ({neutral_pct:.1f}%)")
        
        # Overall sentiment
        if positive_pct > negative_pct:
            overall_sentiment = "POSITIVE"
        elif negative_pct > positive_pct:
            overall_sentiment = "NEGATIVE"
        else:
            overall_sentiment = "NEUTRAL"
            
        results.append(f"\nOverall Sentiment: {overall_sentiment}")
        
        return "\n".join(results)
        
    def extract_keywords(self, data):
        """
        Extract common keywords from feedback
        
        Args:
            data (pandas.DataFrame): Feedback data
            
        Returns:
            str: Keyword analysis results
        """
        results = []
        results.append("=== KEYWORD ANALYSIS RESULTS ===\n")
        
        feedback_col = self.get_feedback_column(data)
        if feedback_col is None:
            return "Error: Could not identify feedback column in data."
            
        # Collect all words
        all_words = []
        for _, row in data.iterrows():
            feedback_text = str(row[feedback_col]).lower()
            # Remove punctuation and split into words
            words = re.findall(r'\b[a-zA-Z]+\b', feedback_text)
            all_words.extend(words)
            
        # Remove common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
        
        filtered_words = [word for word in all_words if word not in stop_words and len(word) > 2]
        
        # Count word frequencies
        word_counts = Counter(filtered_words)
        
        # Get top keywords
        top_keywords = word_counts.most_common(20)
        
        results.append("Top 20 Keywords:")
        results.append("-" * 30)
        
        for word, count in top_keywords:
            results.append(f"{word}: {count} occurrences")
            
        return "\n".join(results)
        
    def identify_topics(self, data):
        """
        Identify common topics in feedback
        
        Args:
            data (pandas.DataFrame): Feedback data
            
        Returns:
            str: Topic analysis results
        """
        results = []
        results.append("=== TOPIC ANALYSIS RESULTS ===\n")
        
        feedback_col = self.get_feedback_column(data)
        if feedback_col is None:
            return "Error: Could not identify feedback column in data."
            
        # Define topic keywords
        topics = {
            'Customer Service': ['service', 'support', 'help', 'assistant', 'representative', 'agent'],
            'Product Quality': ['quality', 'product', 'item', 'goods', 'material', 'durability'],
            'Price/Value': ['price', 'cost', 'expensive', 'cheap', 'value', 'worth', 'money'],
            'Delivery/Shipping': ['delivery', 'shipping', 'arrived', 'package', 'mail', 'transport'],
            'Website/App': ['website', 'app', 'online', 'interface', 'user', 'navigation'],
            'Communication': ['communication', 'email', 'phone', 'message', 'contact', 'response']
        }
        
        topic_counts = {topic: 0 for topic in topics}
        
        for _, row in data.iterrows():
            feedback_text = str(row[feedback_col]).lower()
            
            for topic, keywords in topics.items():
                if any(keyword in feedback_text for keyword in keywords):
                    topic_counts[topic] += 1
                    
        results.append("Topics Mentioned:")
        results.append("-" * 30)
        
        for topic, count in sorted(topic_counts.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                percentage = (count / len(data)) * 100
                results.append(f"{topic}: {count} mentions ({percentage:.1f}%)")
                
        return "\n".join(results)
        
    def generate_summary(self, data):
        """
        Generate a summary of feedback data
        
        Args:
            data (pandas.DataFrame): Feedback data
            
        Returns:
            str: Summary of feedback
        """
        results = []
        results.append("=== FEEDBACK SUMMARY ===\n")
        
        feedback_col = self.get_feedback_column(data)
        if feedback_col is None:
            return "Error: Could not identify feedback column in data."
            
        total_feedback = len(data)
        results.append(f"Total feedback entries: {total_feedback}")
        
        # Average feedback length
        feedback_lengths = [len(str(row[feedback_col])) for _, row in data.iterrows()]
        avg_length = sum(feedback_lengths) / len(feedback_lengths) if feedback_lengths else 0
        results.append(f"Average feedback length: {avg_length:.1f} characters")
        
        # Most common words (for summary)
        all_words = []
        for _, row in data.iterrows():
            feedback_text = str(row[feedback_col]).lower()
            words = re.findall(r'\b[a-zA-Z]+\b', feedback_text)
            all_words.extend(words)
            
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        filtered_words = [word for word in all_words if word not in stop_words and len(word) > 2]
        
        word_counts = Counter(filtered_words)
        top_words = word_counts.most_common(10)
        
        results.append("\nMost common themes:")
        for word, count in top_words:
            results.append(f"- {word} (mentioned {count} times)")
            
        # Quick sentiment overview
        positive_count = 0
        negative_count = 0
        
        for _, row in data.iterrows():
            feedback_text = str(row[feedback_col]).lower()
            positive_words_found = sum(1 for word in self.positive_words if word in feedback_text)
            negative_words_found = sum(1 for word in self.negative_words if word in feedback_text)
            
            if positive_words_found > negative_words_found:
                positive_count += 1
            elif negative_words_found > positive_words_found:
                negative_count += 1
                
        results.append(f"\nQuick Sentiment Overview:")
        results.append(f"- Positive feedback: {positive_count}")
        results.append(f"- Negative feedback: {negative_count}")
        results.append(f"- Neutral feedback: {total_feedback - positive_count - negative_count}")
        
        return "\n".join(results)
        
    def get_feedback_column(self, data):
        """
        Identify the feedback column in the dataset
        
        Args:
            data (pandas.DataFrame): Input data
            
        Returns:
            str: Column name containing feedback
        """
        possible_names = ['feedback', 'review', 'comment', 'text', 'message', 'response']
        
        for col in data.columns:
            if any(name in col.lower() for name in possible_names):
                return col
                
        # If no obvious column name, use the first text column
        for col in data.columns:
            if data[col].dtype == 'object':
                return col
                
        return None 