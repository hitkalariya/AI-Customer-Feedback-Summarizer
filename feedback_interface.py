"""
Feedback Analysis Interface
Provides a graphical user interface for customer feedback analysis
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
from feedback_processor import FeedbackProcessor
from data_visualizer import DataVisualizer

class FeedbackAnalyzerInterface:
    """
    Main interface class for the feedback analysis system
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.processor = FeedbackProcessor()
        self.visualizer = DataVisualizer()
        self.setup_interface()
        
    def setup_window(self):
        """Configure the main window properties"""
        self.root.title("Customer Feedback Analysis System")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Set window icon and styling
        style = ttk.Style()
        style.theme_use('clam')
        
    def setup_interface(self):
        """Create and arrange all interface elements"""
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=60)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="Customer Feedback Analysis System",
            font=("Arial", 16, "bold"),
            fg='white',
            bg='#2c3e50'
        )
        title_label.pack(expand=True)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg='#f0f0f0')
        content_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # File selection section
        self.create_file_section(content_frame)
        
        # Analysis options section
        self.create_analysis_section(content_frame)
        
        # Results display section
        self.create_results_section(content_frame)
        
        # Control buttons
        self.create_control_buttons(content_frame)
        
    def create_file_section(self, parent):
        """Create file selection interface"""
        file_frame = tk.LabelFrame(parent, text="Data Input", bg='#f0f0f0', font=("Arial", 10, "bold"))
        file_frame.pack(fill='x', pady=5)
        
        # File path display
        self.file_path_var = tk.StringVar()
        path_entry = tk.Entry(file_frame, textvariable=self.file_path_var, width=60, state='readonly')
        path_entry.pack(side='left', padx=5, pady=5)
        
        # Browse button
        browse_btn = tk.Button(
            file_frame, 
            text="Browse Files", 
            command=self.browse_file,
            bg='#3498db',
            fg='white',
            font=("Arial", 9)
        )
        browse_btn.pack(side='right', padx=5, pady=5)
        
    def create_analysis_section(self, parent):
        """Create analysis options interface"""
        analysis_frame = tk.LabelFrame(parent, text="Analysis Options", bg='#f0f0f0', font=("Arial", 10, "bold"))
        analysis_frame.pack(fill='x', pady=5)
        
        # Analysis type selection
        tk.Label(analysis_frame, text="Analysis Type:", bg='#f0f0f0').pack(anchor='w', padx=5)
        
        self.analysis_type = tk.StringVar(value="sentiment")
        analysis_options = [
            ("Sentiment Analysis", "sentiment"),
            ("Keyword Extraction", "keywords"),
            ("Topic Modeling", "topics"),
            ("Summary Generation", "summary")
        ]
        
        for text, value in analysis_options:
            tk.Radiobutton(
                analysis_frame, 
                text=text, 
                variable=self.analysis_type, 
                value=value,
                bg='#f0f0f0'
            ).pack(anchor='w', padx=20)
            
    def create_results_section(self, parent):
        """Create results display interface"""
        results_frame = tk.LabelFrame(parent, text="Analysis Results", bg='#f0f0f0', font=("Arial", 10, "bold"))
        results_frame.pack(fill='both', expand=True, pady=5)
        
        # Results text area
        self.results_text = tk.Text(
            results_frame, 
            height=15, 
            width=80,
            font=("Consolas", 9),
            bg='white',
            wrap='word'
        )
        
        # Scrollbar for results
        scrollbar = tk.Scrollbar(results_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        scrollbar.pack(side='right', fill='y', pady=5)
        
    def create_control_buttons(self, parent):
        """Create control buttons"""
        button_frame = tk.Frame(parent, bg='#f0f0f0')
        button_frame.pack(fill='x', pady=10)
        
        # Analyze button
        analyze_btn = tk.Button(
            button_frame,
            text="Start Analysis",
            command=self.start_analysis,
            bg='#27ae60',
            fg='white',
            font=("Arial", 10, "bold"),
            width=15
        )
        analyze_btn.pack(side='left', padx=5)
        
        # Export button
        export_btn = tk.Button(
            button_frame,
            text="Export Results",
            command=self.export_results,
            bg='#e67e22',
            fg='white',
            font=("Arial", 10, "bold"),
            width=15
        )
        export_btn.pack(side='left', padx=5)
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="Clear Results",
            command=self.clear_results,
            bg='#e74c3c',
            fg='white',
            font=("Arial", 10, "bold"),
            width=15
        )
        clear_btn.pack(side='right', padx=5)
        
    def browse_file(self):
        """Open file dialog for data selection"""
        file_types = [
            ('CSV files', '*.csv'),
            ('Text files', '*.txt'),
            ('Excel files', '*.xlsx'),
            ('All files', '*.*')
        ]
        
        filename = filedialog.askopenfilename(
            title="Select Feedback Data File",
            filetypes=file_types
        )
        
        if filename:
            self.file_path_var.set(filename)
            
    def start_analysis(self):
        """Start the analysis process in a separate thread"""
        if not self.file_path_var.get():
            messagebox.showerror("Error", "Please select a data file first!")
            return
            
        # Disable buttons during analysis
        self.root.config(cursor="wait")
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self.perform_analysis)
        thread.daemon = True
        thread.start()
        
    def perform_analysis(self):
        """Perform the actual analysis"""
        try:
            file_path = self.file_path_var.get()
            analysis_type = self.analysis_type.get()
            
            # Process the data
            results = self.processor.analyze_feedback(file_path, analysis_type)
            
            # Update UI in main thread
            self.root.after(0, self.display_results, results)
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Analysis Error", str(e)))
        finally:
            self.root.after(0, lambda: self.root.config(cursor=""))
            
    def display_results(self, results):
        """Display analysis results in the text area"""
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results)
        
    def export_results(self):
        """Export results to a file"""
        if not self.results_text.get(1.0, tk.END).strip():
            messagebox.showwarning("Warning", "No results to export!")
            return
            
        filename = filedialog.asksaveasfilename(
            title="Save Results",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.results_text.get(1.0, tk.END))
                messagebox.showinfo("Success", "Results exported successfully!")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export: {e}")
                
    def clear_results(self):
        """Clear the results display"""
        self.results_text.delete(1.0, tk.END)
        
    def start_application(self):
        """Start the main application loop"""
        self.root.mainloop() 