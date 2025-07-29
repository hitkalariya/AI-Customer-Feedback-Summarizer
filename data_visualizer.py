"""
Data Visualization Module
Provides functionality for creating charts and graphs from feedback analysis
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
from collections import Counter
import tkinter as tk
from tkinter import ttk

class DataVisualizer:
    """
    Class for creating various types of visualizations from feedback data
    """
    
    def __init__(self):
        self.colors = {
            'positive': '#2ecc71',
            'negative': '#e74c3c',
            'neutral': '#95a5a6',
            'primary': '#3498db',
            'secondary': '#f39c12',
            'accent': '#9b59b6'
        }
        self.figure = None
        self.canvas = None
        
    def create_sentiment_chart(self, positive_count, negative_count, neutral_count, parent_frame):
        """
        Create a pie chart showing sentiment distribution
        
        Args:
            positive_count (int): Number of positive feedback
            negative_count (int): Number of negative feedback
            neutral_count (int): Number of neutral feedback
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(8, 6), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Data for pie chart
        sizes = [positive_count, negative_count, neutral_count]
        labels = ['Positive', 'Negative', 'Neutral']
        colors = [self.colors['positive'], self.colors['negative'], self.colors['neutral']]
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(
            sizes, 
            labels=labels, 
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            explode=(0.05, 0.05, 0.05)
        )
        
        # Customize text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            
        ax.set_title('Sentiment Distribution', fontsize=16, fontweight='bold', pad=20)
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def create_keyword_bar_chart(self, keywords_data, parent_frame):
        """
        Create a horizontal bar chart for keyword frequencies
        
        Args:
            keywords_data (list): List of tuples (keyword, count)
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(10, 8), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Prepare data
        keywords, counts = zip(*keywords_data[:15])  # Top 15 keywords
        
        # Create horizontal bar chart
        y_pos = np.arange(len(keywords))
        bars = ax.barh(y_pos, counts, color=self.colors['primary'])
        
        # Customize chart
        ax.set_yticks(y_pos)
        ax.set_yticklabels(keywords)
        ax.set_xlabel('Frequency', fontweight='bold')
        ax.set_title('Top Keywords in Feedback', fontsize=16, fontweight='bold', pad=20)
        
        # Add value labels on bars
        for i, (bar, count) in enumerate(zip(bars, counts)):
            width = bar.get_width()
            ax.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                   str(count), ha='left', va='center', fontweight='bold')
        
        # Invert y-axis to show highest frequency at top
        ax.invert_yaxis()
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def create_topic_chart(self, topic_data, parent_frame):
        """
        Create a bar chart for topic analysis
        
        Args:
            topic_data (dict): Dictionary of topic names and their counts
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(10, 6), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Prepare data
        topics = list(topic_data.keys())
        counts = list(topic_data.values())
        
        # Create bar chart
        bars = ax.bar(topics, counts, color=self.colors['secondary'])
        
        # Customize chart
        ax.set_xlabel('Topics', fontweight='bold')
        ax.set_ylabel('Mentions', fontweight='bold')
        ax.set_title('Topic Analysis', fontsize=16, fontweight='bold', pad=20)
        
        # Rotate x-axis labels for better readability
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                   str(count), ha='center', va='bottom', fontweight='bold')
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def create_feedback_length_histogram(self, feedback_lengths, parent_frame):
        """
        Create a histogram showing distribution of feedback lengths
        
        Args:
            feedback_lengths (list): List of feedback character lengths
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(10, 6), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Create histogram
        n, bins, patches = ax.hist(feedback_lengths, bins=20, color=self.colors['accent'], 
                                  alpha=0.7, edgecolor='black')
        
        # Customize chart
        ax.set_xlabel('Feedback Length (characters)', fontweight='bold')
        ax.set_ylabel('Frequency', fontweight='bold')
        ax.set_title('Feedback Length Distribution', fontsize=16, fontweight='bold', pad=20)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Add statistics text
        mean_length = np.mean(feedback_lengths)
        median_length = np.median(feedback_lengths)
        ax.axvline(mean_length, color='red', linestyle='--', linewidth=2, 
                   label=f'Mean: {mean_length:.1f}')
        ax.axvline(median_length, color='green', linestyle='--', linewidth=2, 
                   label=f'Median: {median_length:.1f}')
        ax.legend()
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def create_trend_chart(self, data_points, labels, parent_frame):
        """
        Create a line chart showing trends over time
        
        Args:
            data_points (list): List of numerical data points
            labels (list): List of labels for x-axis
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(10, 6), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Create line chart
        ax.plot(labels, data_points, marker='o', linewidth=2, 
                color=self.colors['primary'], markersize=8)
        
        # Customize chart
        ax.set_xlabel('Time Period', fontweight='bold')
        ax.set_ylabel('Feedback Count', fontweight='bold')
        ax.set_title('Feedback Trends Over Time', fontsize=16, fontweight='bold', pad=20)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        # Rotate x-axis labels if needed
        if len(labels) > 5:
            plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def create_comparison_chart(self, categories, values1, values2, label1, label2, parent_frame):
        """
        Create a grouped bar chart for comparing two sets of data
        
        Args:
            categories (list): List of category names
            values1 (list): First set of values
            values2 (list): Second set of values
            label1 (str): Label for first dataset
            label2 (str): Label for second dataset
            parent_frame: Tkinter frame to embed the chart
            
        Returns:
            matplotlib.figure.Figure: The created figure
        """
        # Create figure and axis
        self.figure = Figure(figsize=(12, 6), facecolor='white')
        ax = self.figure.add_subplot(111)
        
        # Set up bar positions
        x = np.arange(len(categories))
        width = 0.35
        
        # Create grouped bars
        bars1 = ax.bar(x - width/2, values1, width, label=label1, color=self.colors['primary'])
        bars2 = ax.bar(x + width/2, values2, width, label=label2, color=self.colors['secondary'])
        
        # Customize chart
        ax.set_xlabel('Categories', fontweight='bold')
        ax.set_ylabel('Values', fontweight='bold')
        ax.set_title('Comparison Analysis', fontsize=16, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(categories)
        ax.legend()
        
        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                       f'{height:.1f}', ha='center', va='bottom', fontsize=8)
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, parent_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
        return self.figure
        
    def clear_canvas(self):
        """Clear the current canvas"""
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        if self.figure:
            plt.close(self.figure)
            self.figure = None
            
    def save_chart(self, filename):
        """
        Save the current chart to a file
        
        Args:
            filename (str): Path where to save the chart
        """
        if self.figure:
            self.figure.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"Chart saved to {filename}")
        else:
            print("No chart to save") 

    def export_all_charts_as_zip(self, charts, filenames, zip_filename):
        """
        Export multiple chart figures as images and compress them into a zip file.

        Args:
            charts (list): List of matplotlib.figure.Figure objects.
            filenames (list): List of filenames for each chart image.
            zip_filename (str): Output zip file name.
        """
        import zipfile
        import io
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for fig, fname in zip(charts, filenames):
                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                buf.seek(0)
                zipf.writestr(fname, buf.read())
        print(f"Exported {len(charts)} charts to {zip_filename}") 