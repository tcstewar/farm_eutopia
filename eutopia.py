import map
import activity


class Farm:
    def __init__(self, id, county, lat, long, area, land_type):
        self.id = id
        self.land_type = land_type
        self.county = county
        self.lat = lat
        self.long = long
        self.area = area
        
        self.activity = None
        self.state = 'unplanted'
        

class Family:
    def __init__(self, eutopia):
        self.eutopia = eutopia
        self.farms = []
        self.bank_balance = 1000000.00
        self.equipment = []
        self.preferences = {'money': 1}
        
    def make_planting_decision(self, activities, farm):    
        best = None
        for activity in activities:
            total = 0
            for pref, weight in self.preferences.items():
                total += activity.get_product(pref, farm) * weight
                # TODO: improve choice algorithm
                #    - maybe by allowing different sensitivities to risk
                #      on different income dimensions
                
            if best is None or total > best_total:
                best = activity
                best_total = total
                
        farm.activity = best
        farm.state = 'planted'        
        
    
    def step(self):
        for farm in self.farms:
            if farm.state == 'unplanted':
                self.make_planting_decision(eutopia.activities, farm)


class Eutopia:
    def __init__(self):
        self.map = map.Map('guatemala.json')
        
        self.activities = activity.Activities().activities
        
        self.farms = []
        for farm_data in self.map.farms:
            farm = Farm(*farm_data)
            self.farms.append(farm)
            
        self.families = []
        for farm in self.farms:
            family = Family(self)
            family.farms.append(farm)
            self.families.append(family)
            
    def step(self):
        for family in self.families:
            family.step()
            
        
        
if __name__=='__main__':
    eutopia = Eutopia()
    
    eutopia.step()
    
    for farm in eutopia.farms[:10]:
        print farm.state, farm.activity.name