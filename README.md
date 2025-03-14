Project Overview:-

This project is an Automated PDF Report Generator built using Python. It reads sales data from a CSV file, generates a sales summary, creates a sales chart, and compiles the results into a formatted PDF report.

Features:-

Load sales data from a CSV file.

Calculate total sales and determine the top-performing product.

Generate a bar chart visualizing sales per product.

Create a well-structured PDF report containing the summary and chart.

Technologies Used:-

Python:-

Pandas (for data processing)

Matplotlib (for data visualization)

FPDF (for PDF generation)

Project Structure:-
AutomatedPDFReportGenerator/
│-- sales_data.csv              # Sample sales data (replace with your own)
│-- sales_report.py             # Main Python script
│-- sales_chart.png             # Generated sales chart
│-- sales_report.pdf            # Final report
│-- README.md                   # Project documentation

How to Run the Project:-

Install Dependencies:-

Before running the script, install the required Python libraries:
pip install pandas matplotlib fpdf

 Add Your Sales Data:-

Replace sales_data.csv with your own dataset containing at least:
Product,Sales
Product A,1200
Product B,2300
Product C,3100

Run the Script:-

Execute the Python script to generate the report:
python sales_report.py

View the Report:-

The generated sales_chart.png will visualize the sales.

The final sales_report.pdf will contain the summary and the chart.

Example Output:-

Total Sales: $6,600

Top Product: Product C

Generated PDF:

Contributing:-

Feel free to fork this repository, submit issues, and make pull requests!

Created by Shaivi Singh
