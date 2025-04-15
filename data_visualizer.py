import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_models(top_models):
    plt.figure(figsize=(10, 6))
    top_models.plot(kind='barh', color='skyblue')
    plt.title('Top 10 Most Listed Car Models')
    plt.xlabel('Number of Listings')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def plot_pie_charts(trans_dist, fuel_dist):
    plt.figure(figsize=(6, 6))
    trans_dist.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Transmission Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(6, 6))
    fuel_dist.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette("pastel"))
    plt.title('Fuel Type Distribution')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()
