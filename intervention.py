class PriceIntervention:
    def __init__(self, time, product, scale, phase_in_time=0):
        self.time = time
        self.product = product
        self.scale = scale
        self.phase_in_time = phase_in_time
        self.original_value = None
        
    def apply(self, eutopia, time):
        assert time>=self.time
        
        money = eutopia.activities.aggregates['money']
        
        if self.original_value is None:
            self.original_value = money[self.product]
        
        scale = self.scale
        if self.phase_in_time>0:
            ratio = float(time-self.time)/phase_in_time
            if ratio>1: ratio = 1
            scale = scale*ratio    
        
        money[self.product] = self.original_value*scale
            