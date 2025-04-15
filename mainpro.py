from data_loader import load_dataset
from data_cleaner import clean_data
from data_analysis import analyze_data
from data_visualizer import plot_top_models, plot_pie_charts
from db_config import get_connection
from db_insert import insert_into_db

def main():
    df = load_dataset("uae_used_cars.csv")
    df = clean_data(df)
    
    top_models, trans_dist, fuel_dist = analyze_data(df)
    
    plot_top_models(top_models)
    plot_pie_charts(trans_dist, fuel_dist)
    
    conn = get_connection()
    insert_into_db(df, conn)
    conn.close()

if __name__ == "__main__":
    main()
