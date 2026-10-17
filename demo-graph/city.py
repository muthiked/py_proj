from app import db

class Post(db.Model):
    db.Column("id",db.Integer,primary_key=True)
    name = db.Column("name",db.String)
    countyCode = db.Column("countyCode",db.String)
    district = db.Column("district",db.String)
    population = db.Column("population",db.Integer)

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "countyCode":self.countyCode,
            "district":self.district,
            "population":self.population
        }