from flask import Flask, render_template, request
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

# Inisialisasi Flask
app = Flask(__name__)

# Load model
model = joblib.load('final_delivery_time_model.joblib')

# Kolom model sesuai training
model_columns = [
    'Distance_km', 'Preparation_Time_min', 'Courier_Experience_yrs',
    'Weather_Foggy', 'Weather_Rainy', 'Weather_Snowy', 'Weather_Windy',
    'Traffic_Level_Low', 'Traffic_Level_Medium',
    'Time_of_Day_Evening', 'Time_of_Day_Morning', 'Time_of_Day_Night',
    'Vehicle_Type_Car', 'Vehicle_Type_Scooter'
]

# Load dataset mentah
df = pd.read_csv('Food_Delivery_Times.csv')

# Encode kategori menjadi biner untuk prediksi
df_encoded = pd.get_dummies(df,
                            columns=["Weather", "Traffic_Level",
                                     "Time_of_Day", "Vehicle_Type"],
                            drop_first=False)

# Fungsi membuat scatterplot


def create_scatter(df, x, y, title):
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=x, y=y, data=df, alpha=0.5)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    return plot

# Route utama: prediksi + scatterplot


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction_text = ""
    if request.method == 'POST':
        distance = request.form['distance']
        prep_time = request.form['prep_time']
        experience = request.form['experience']
        weather = request.form['weather']
        traffic = request.form['traffic']
        time_of_day = request.form['time_of_day']
        vehicle = request.form['vehicle']

        try:
            distance = float(distance)
            prep_time = float(prep_time)
            experience = float(experience)
            if distance < 0 or prep_time < 0 or experience < 0:
                prediction_text = "❌ Masukkan nilai positif!"
            else:
                valid_weathers = ["Foggy", "Rainy", "Snowy", "Windy"]
                valid_traffic = ["Low", "Medium"]
                valid_times = ["Evening", "Morning", "Night"]
                valid_vehicles = ["Car", "Scooter"]

                if weather not in valid_weathers or traffic not in valid_traffic \
                        or time_of_day not in valid_times or vehicle not in valid_vehicles:
                    prediction_text = "❌ Pilihan kategori tidak valid!"
                else:
                    data = {
                        'Distance_km': [distance],
                        'Preparation_Time_min': [prep_time],
                        'Courier_Experience_yrs': [experience],
                        'Weather_Foggy': [1 if weather == "Foggy" else 0],
                        'Weather_Rainy': [1 if weather == "Rainy" else 0],
                        'Weather_Snowy': [1 if weather == "Snowy" else 0],
                        'Weather_Windy': [1 if weather == "Windy" else 0],
                        'Traffic_Level_Low': [1 if traffic == "Low" else 0],
                        'Traffic_Level_Medium': [1 if traffic == "Medium" else 0],
                        'Time_of_Day_Evening': [1 if time_of_day == "Evening" else 0],
                        'Time_of_Day_Morning': [1 if time_of_day == "Morning" else 0],
                        'Time_of_Day_Night': [1 if time_of_day == "Night" else 0],
                        'Vehicle_Type_Car': [1 if vehicle == "Car" else 0],
                        'Vehicle_Type_Scooter': [1 if vehicle == "Scooter" else 0]
                    }
                    input_df = pd.DataFrame(data)
                    input_df = input_df.reindex(
                        columns=model_columns, fill_value=0)
                    pred = model.predict(input_df)[0]
                    prediction_text = f"⏱️ Perkiraan waktu pengiriman: {round(pred, 2)} menit"
        except:
            prediction_text = "❌ Masukkan input yang valid!"

    # Scatterplot
    plot1 = create_scatter(df, 'Distance_km', 'Delivery_Time_min',
                           'Hubungan Jarak vs Waktu Pengiriman')

    return render_template('index.html', prediction_text=prediction_text, plot1=plot1)


# Jalankan Flask
if __name__ == '__main__':
    app.run(debug=True)
