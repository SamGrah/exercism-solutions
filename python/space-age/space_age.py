class SpaceAge:
    def __init__(self, seconds):
        seconds_to_years = 1 / 31_557_600
        self.earth_age = seconds * seconds_to_years

    def on_earth(self):
        return round(self.earth_age, 2)

    def on_mercury(self):
        mercury_age = self.earth_age / 0.2408467
        return round(mercury_age, 2)

    def on_venus(self):
        venus_age = self.earth_age / 0.61519726
        return round(venus_age, 2)

    def on_mars(self):
        mars_age = self.earth_age / 1.8808158
        return round(mars_age, 2)

    def on_jupiter(self):
        jupiter_age = self.earth_age / 11.862615
        return round(jupiter_age, 2)

    def on_saturn(self):
        saturn_age = self.earth_age / 29.447498
        return round(saturn_age, 2)

    def on_uranus(self):
        uranus_age = self.earth_age / 84.016846
        return round(uranus_age, 2)

    def on_neptune(self):
        neptune_age = self.earth_age / 164.79132
        return round(neptune_age, 2)
