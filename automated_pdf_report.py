print("✅ Python script is running!")
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def load_data(file_path):
    """Load sales data from CSV."""
    return pd.read_csv(file_path)

def generate_sales_summary(df):
    """Generate total sales and top product summary."""
    total_sales = df["Sales"].sum()
    top_product = df.groupby("Product")["Sales"].sum().idxmax()
    return total_sales, top_product

def generate_sales_chart(df, output_path):
    """Create and save a sales chart."""
    sales_by_product = df.groupby("Product")["Sales"].sum()
    plt.figure(figsize=(6, 4))
    sales_by_product.plot(kind="bar", color="skyblue")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

class PDFReport(FPDF):
    """Custom PDF Report class."""
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Sales Report", ln=True, align="C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(summary, chart_path, output_pdf):
    """Generate the final PDF report."""
    pdf = PDFReport()
    pdf.add_page()
    
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, "Sales Summary", ln=True, align="L")
    
    pdf.set_font("Arial", "", 12)
    total_sales, top_product = summary
    pdf.multi_cell(0, 10, f"Total Sales: ${total_sales}\nTop Product: {top_product}")
    
    pdf.image(chart_path, x=10, y=50, w=180)
    pdf.output(output_pdf)

def main():
    """Main function to run the report generator."""
    data_file = "sales_data.csv"  # Update with your file path
    chart_file = "sales_chart.png"
    pdf_file = "sales_report.pdf"
    
    if not os.path.exists(data_file):
        print("Error: CSV file not found!")
        return
    
    print("Loading data from CSV...")
    df = load_data(data_file)
    print("Generating summary...")
    summary = generate_sales_summary(df)
    print("creating sales chart...")
    generate_sales_chart(df, chart_file)
    print("Generating PDF report...")
    generate_pdf_report(summary, chart_file, pdf_file)
    
    print(f"Report generated: {pdf_file}")

if __name__ == "__main__":git init

    main()

