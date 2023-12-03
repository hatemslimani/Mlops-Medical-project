class AccidentModel:
    def __init__(self, ID, Source, Severity, Start_Time, End_Time, Start_Lat, Start_Lng, Distance, Description, Street, City, County, State, Zipcode, Country, Timezone, Airport_Code, Weather_Timestamp, Temperature_F, Wind_Chill_F, Humidity, Pressure, Visibility_mi, Wind_Direction, Wind_Speed_mph, Precipitation, Weather_Condition, Amenity, Bump, Crossing, Give_Way, Junction, No_Exit, Railway, Roundabout, Station, Stop, Traffic_Calming, Traffic_Signal, Turning_Loop, Sunrise_Sunset, Civil_Twilight, Nautical_Twilight, Astronomical_Twilight):
        self.ID = ID
        self.Source = Source
        self.Severity = Severity
        self.Start_Time = Start_Time
        self.End_Time = End_Time
        self.Start_Lat = Start_Lat
        self.Start_Lng = Start_Lng
        self.Distance = Distance
        self.Description = Description
        self.Street = Street
        self.City = City
        self.County = County
        self.State = State
        self.Zipcode = Zipcode
        self.Country = Country
        self.Timezone = Timezone
        self.Airport_Code = Airport_Code
        self.Weather_Timestamp = Weather_Timestamp
        self.Temperature_F = Temperature_F
        self.Wind_Chill_F = Wind_Chill_F
        self.Humidity = Humidity
        self.Pressure = Pressure
        self.Visibility_mi = Visibility_mi
        self.Wind_Direction = Wind_Direction
        self.Wind_Speed_mph = Wind_Speed_mph
        self.Precipitation = Precipitation
        self.Weather_Condition = Weather_Condition
        self.Amenity = Amenity
        self.Bump = Bump
        self.Crossing = Crossing
        self.Give_Way = Give_Way
        self.Junction = Junction
        self.No_Exit = No_Exit
        self.Railway = Railway
        self.Roundabout = Roundabout
        self.Station = Station
        self.Stop = Stop
        self.Traffic_Calming = Traffic_Calming
        self.Traffic_Signal = Traffic_Signal
        self.Turning_Loop = Turning_Loop
        self.Sunrise_Sunset = Sunrise_Sunset
        self.Civil_Twilight = Civil_Twilight
        self.Nautical_Twilight = Nautical_Twilight
        self.Astronomical_Twilight = Astronomical_Twilight

    def __str__(self):
        return f"ID: {self.ID}, Source: {self.Source}, Severity: {self.Severity}, Start_Time: {self.Start_Time}, End_Time: {self.End_Time}, Start_Lat: {self.Start_Lat}, Start_Lng: {self.Start_Lng}, Distance: {self.Distance}, Description: {self.Description}, Street: {self.Street}, City: {self.City}, County: {self.County}, State: {self.State}, Zipcode: {self.Zipcode}, Country: {self.Country}, Timezone: {self.Timezone}, Airport_Code: {self.Airport_Code}, Weather_Timestamp: {self.Weather_Timestamp}, Temperature_F: {self.Temperature_F}, Wind_Chill_F: {self.Wind_Chill_F}, Humidity: {self.Humidity}, Pressure: {self.Pressure}, Visibility_mi: {self.Visibility_mi}, Wind_Direction: {self.Wind_Direction}, Wind_Speed_mph: {self.Wind_Speed_mph}, Precipitation: {self.Precipitation}, Weather_Condition: {self.Weather_Condition}, Amenity: {self.Amenity}, Bump: {self.Bump}, Crossing: {self.Crossing}, Give_Way: {self.Give_Way}, Junction: {self.Junction}, No_Exit: {self.No_Exit}, Railway: {self.Railway}, Roundabout: {self.Roundabout}, Station: {self.Station}, Stop: {self.Stop}, Traffic_Calming: {self.Traffic_Calming}, Traffic_Signal: {self.Traffic_Signal}, Turning_Loop: {self.Turning_Loop}, Sunrise_Sunset: {self.Sunrise_Sunset}, Civil_Twilight: {self.Civil_Twilight}, Nautical_Twilight: {self.Nautical_Twilight}, Astronomical_Twilight: {self.Astronomical_Twilight}"
