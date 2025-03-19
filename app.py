from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the Excel data
excel_file = 'products.xlsx'  # Update the path to your Excel file accordingly
df = pd.read_excel(excel_file)

# Ensure the column names are correct
df.columns = ['ProductID', 'ProductCode', 'ProductName', 'ProductDescription', 'UnitPrice']

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_products = pd.DataFrame()  # Default empty DataFrame

    if request.method == 'POST':
        selected_product_names = request.form.getlist('product_name')  # List of selected product names
        selected_products = df[df['ProductName'].isin(selected_product_names)]  # Filter DataFrame based on selected product names

    # Extract unique product names for checkboxes
    product_names = df['ProductName'].unique()

    return render_template('index.html', product_names=product_names, selected_products=selected_products)

if __name__ == '__main__':
    app.run(debug=True)
