import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

#Because I have an @ symbol in my password, there is a chance the connection string will break due to the string syntax already containing an @ symbol.
from urllib.parse import quote_plus

# Suppress SQLAlchemy warnings that don't affect functionality
warnings.filterwarnings('ignore', category=sqlalchemy.exc.SAWarning)
# Suppress deprecation warnings to reduce noise during development
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Database connection configuration
DB_CONFIG = {
    'server': 'azuresqldbserverken.database.windows.net',
    'database': 'kenAzureSQLdb',
    'username': 'CLoudSAee97d938',
    'password': quote_plus('@Godsent1man'), # This correctly handles the @ symbol
    'driver': 'ODBC Driver 17 for SQL Server'
}

# Construct SQLAlchemy connection string for SQL Server
DB_URL = f"mssql+pyodbc://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['server']}/{DB_CONFIG['database']}?driver={DB_CONFIG['driver']}"

# Define table name for the planetary analysis data
TABLE_NAME = 'planetary_analysis'

# Status message for debugging connection issues
print("Connecting to the database and loading data...")

try:
    # Create SQLAlchemy engine for database connection
    engine = sqlalchemy.create_engine(DB_URL)
    # Establish connection to the database
    connection = engine.connect()
    
    # Define columns needed for correlation analysis
    columns_for_correlation = [
        'mass',
        'radius',
        'orbital_period',
        'semi_major_axis',
        'temp_calculated',
        'star_mass',
        'star_teff',
        'discovered'
    ]
    
    # Add SQL Server bracket notation to column names for safe querying
    quoted_columns = [f'[{col}]' for col in columns_for_correlation]
    # Construct SQL query to retrieve specified columns
    query = f"SELECT {', '.join(quoted_columns)} FROM [dbo].[{TABLE_NAME}]"
    
    # Execute query and load data into pandas DataFrame
    df = pd.read_sql(query, connection)
    # Success message with data dimensions for debugging
    print(f"Data loaded successfully. {len(df)} rows and {len(df.columns)} columns selected for analysis.")
    
except Exception as e:
    # Error handling with detailed information for debugging
    print(f"Error connecting to database or loading data: {e}")
    print("Please ensure your database configuration is correct and the necessary DB driver is installed.")
    print(f"SQLAlchemy URL attempted: {DB_URL}")
    exit()
finally:
    # Ensure database connection is properly closed to prevent resource leaks
    if 'connection' in locals() and connection:
        connection.close()

# Display null value information to understand data quality before correlation
print("\n--- Null Value Information (before correlation) ---")
print(df.isnull().sum())
print("\nNote: .corr() handles nulls by pairwise deletion (only uses non-null pairs).")

# Calculate correlation matrix for numerical analysis
correlation_matrix = df.corr()

# Display formatted correlation matrix for analysis
print("\n--- Correlation Matrix (Numerical Values) ---")
print(correlation_matrix.round(2).to_string())

# Generate correlation heatmap visualization
print("\n--- Generating Correlation Heatmap ---")

# Adjust figure size based on the number of columns for optimal readability
num_cols = len(correlation_matrix.columns)
figsize_width = max(8, num_cols * 1.0)  # Base width 8, then scale up by 1.0 per column
figsize_height = max(6, num_cols * 0.9)  # Base height 6, then scale up by 0.9 per column

# Create the heatmap figure
plt.figure(figsize=(figsize_width, figsize_height))
sns.heatmap(
    correlation_matrix,
    annot=True,        # Show correlation values on the heatmap
    cmap='coolwarm',   # Diverging colormap for correlations (positive/negative)
    fmt=".2f",         # Format annotation values to 2 decimal places
    linewidths=.5,     # Add lines between cells for better visual separation
    vmin=-1,           # Set minimum value for color scale to -1 (perfect negative correlation)
    vmax=1,            # Set maximum value for color scale to 1 (perfect positive correlation)
    center=0           # Set center of color scale to 0 (no correlation)
)

# Format the plot for better readability
plt.title('Correlation Matrix Heatmap for Core Planetary Data', fontsize=16)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels to avoid overlap
plt.yticks(rotation=0)               # Keep y-axis labels horizontal
plt.tight_layout()                   # Adjust layout to prevent labels from being cut off

# Display the plot
print("Heatmap generated. It will appear in a separate window or inline if using a Jupyter Notebook.")
plt.show()

print("\nAnalysis complete.")