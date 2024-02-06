import time
import requests

class IrrigationBasic:
    def __init__(self, max_moisture=100, min_moisture=50, rain_threshold=0.2, et_threshold=0.3, flow_factor=1, tube_constant=5):
        self.max_moisture = max_moisture
        self.min_moisture = min_moisture
        self.current_moisture = 40  # Initial moisture level
        self.rain_threshold = rain_threshold  # Rainfall threshold for not irrigating
        self.et_threshold = et_threshold  # ET threshold for not irrigating
        self.flow_factor = flow_factor  # Pump flow factor for irrigation calculation
        self.tube_constant = tube_constant  # Tube constant for irrigation calculation
        self.base_url = f'https://api.open-meteo.com/v1/forecast?latitude=52.3793&longitude=1.5615&hourly=precipitation_probability,precipitation,et0_fao_evapotranspiration&timezone=Europe%2FLondon&past_hours=1&forecast_days=1&forecast_hours=1'


    def read_moisture_sensor(self):
        # Simulated moisture reading, replace with actual sensor reading
        return self.current_moisture

    def get_weather_data(self):
        url = f"{self.base_url}"
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            data = data['hourly']
            return data
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")
            return None

    def should_irrigate(self):
        weather_data = self.get_weather_data()

        if weather_data is None:
            print("Weather data not available. Cannot determine irrigation status.")
            return False
        
        # Extract relevant information from the response
        xi = weather_data['precipitation_probability'][-1]
        p_hat = weather_data['precipitation'][-1]
        e_hat = weather_data['et0_fao_evapotranspiration'][-1]

        if p_hat > self.rain_threshold:
            print("It's raining. No need for irrigation.")
            return False

        if e_hat > self.et_threshold:
            print("Evapotranspiration is high. No need for irrigation.")
            return False

        return True

    def irrigate(self):
        moisture_level = self.read_moisture_sensor()
        irrigation_time = (self.min_moisture - moisture_level) * self.flow_factor + self.tube_constant
        print(f"Irrigating for {irrigation_time} seconds...")
        time.sleep(irrigation_time)
        print("Irrigation completed.")

    def control_irrigation(self):
        if self.should_irrigate():
            moisture_level = self.read_moisture_sensor()
            if moisture_level < self.min_moisture:
                print("Moisture level is low. Initiating irrigation.")
                self.irrigate()
                self.current_moisture = self.min_moisture # self.read_moisture_sensor()  # Reset moisture level after irrigation
            else:
                print("Moisture level is sufficient. No need for irrigation.")
        else:
            print("No need for irrigation based on weather conditions.")


if __name__ == "__main__":
    irrigation_system = IrrigationBasic()

    try:
        while True:
            irrigation_system.control_irrigation()
            time.sleep(10)  # Check soil moisture level every 10 seconds
    except KeyboardInterrupt:
        print("Exiting...")