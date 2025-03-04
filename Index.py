import pandas as pd
import numpy as np
import webbrowser

# Load Cleaned Data
cleaned_df = pd.read_csv("cleaned_data.csv")

# Convert DataFrame to HTML with styling
html_content = cleaned_df.to_html(classes="table table-bordered", index=False)

# Full HTML Template
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaned Data</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h2 class="text-center">📊 Cleaned Data</h2>
    <div class="table-responsive">
        {html_content}
    </div>
</body>
</html>
"""

# Save as HTML file
html_file_path = "cleaned_data.html"
with open(html_file_path, "w", encoding="utf-8") as file:
    file.write(html_template)

# Open in the default web browser
webbrowser.open(html_file_path)

print(f"\n✅ Cleaned data displayed in: {html_file_path}")
