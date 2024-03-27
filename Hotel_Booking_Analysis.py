import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
hotel_df = pd.read_excel('hotel_bookings.xlsx')

# Display the first few rows of the dataset
print(hotel_df.head())

# Summary statistics for numerical variables
print("\nSummary statistics for numerical variables:")
print(hotel_df.describe())

# Check for missing values
print("\nMissing values:")
print(hotel_df.isnull().sum())

# Visualize the distribution of bookings by hotel type
plt.figure(figsize=(8, 6))
sns.countplot(x='hotel', data=hotel_df)
plt.title('Distribution of Bookings by Hotel Type')
plt.xlabel('Hotel Type')
plt.ylabel('Number of Bookings')
plt.show()

# Visualize the relationship between lead time and booking cancellation
plt.figure(figsize=(8, 6))
sns.scatterplot(x='lead_time', y='is_canceled', data=hotel_df)
plt.title('Correlation between Lead Time and Booking Cancellation')
plt.xlabel('Lead Time (days)')
plt.ylabel('Booking Cancellation (0: Not Canceled, 1: Canceled)')
plt.show()

# Analyze the average number of special requests by hotel type
plt.figure(figsize=(8, 6))
sns.barplot(x='hotel', y='total_of_special_requests', data=hotel_df)
plt.title('Average Number of Special Requests by Hotel Type')
plt.xlabel('Hotel Type')
plt.ylabel('Average Number of Special Requests')
plt.show()

# Identify the busiest months for bookings
plt.figure(figsize=(10, 6))
sns.countplot(x='arrival_date_month', data=hotel_df, order=hotel_df['arrival_date_month'].value_counts().index[:3])
plt.title('Busiest Months for Bookings')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()

# Additional analysis and visualization as needed
