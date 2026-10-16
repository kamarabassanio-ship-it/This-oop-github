import datetime
class FarmCrop:
    def __init__(self, crop_id: str, crop_type: str, plot_area_hectares: float):
        self.crop_id = crop_id
        self.crop_type = crop_type
        self.plot_area_hectares = plot_area_hectares
        self.total_yield_kg = 0.0

# INSTANCE METHOD FOR ADDING HARVEST YIELD
    def add_harvest_yield(self, yield_amount_kg: float) -> None:
        
        if yield_amount_kg > 0:
            self.total_yield_kg += yield_amount_kg
            print(f"--> [Crop {self.crop_id}] Added {yield_amount_kg} kg harvest of {self.crop_type}.")


    def display_crop_summary(self) -> None:
        yield_per_hectare = self.total_yield_kg / self.plot_area_hectares if self.plot_area_hectares > 0 else 0
        print(f"[Plot {self.crop_id}] {self.crop_type} | Area: {self.plot_area_hectares} ha | Total: {self.total_yield_kg} kg ({yield_per_hectare:.1f} kg/ha)")


# CLASS REPRESENTING LIVESTOCK RECORD TRACKING
class LivestockRecord:
    total_livestock_count = 0

    def __init__(self, tag_id: str, animal_type: str, district: str):
        self.tag_id = tag_id
        self.animal_type = animal_type      
        self.district = district            
        
    #   TUPPLE BASED DATA STRUCTURE FOR HEALTH HISTROY
        self.health_history: list[tuple[str, float, str, str]] = []
        
        LivestockRecord.total_livestock_count += 1

        
    #   INSTANCE METHOD TO UPDATE GENERAL LIVESTOCK DETAILS 
    def update_record(self, animal_type: str = None, district: str = None) -> None:
      
        if animal_type:
            self.animal_type = animal_type
        if district:
            self.district = district
        print(f"--> Record updated for Tag ID: {self.tag_id}")

    def log_health_check(self, status: str, weight_kg: float, vaccinated: bool) -> None:
   
         #    INSTANCE METHOD TO RECORD HEALTH ASSAMENT
        today_str = datetime.date.today().isoformat()
        vax_str = "Vaccinated" if vaccinated else "Pending Vaccination"
        
        
        # IMMUTABLE TUPPLE ENTRY FOR  HEALTH HISTROY
        health_entry = (status, weight_kg, vax_str, today_str)
        self.health_history.append(health_entry)
        print(f"--> [HEALTH LOGGED] Tag ID: {self.tag_id} | Status: {status} | Weight: {weight_kg}kg | {vax_str}")

    # INSTANC METHOD TO DISPLAY LIVESTOCK DETAILS AND HEALTH HISTROY
    def display_info(self) -> None:
        print("-" * 60)
        print(f"LIVESTOCK TAG ID : {self.tag_id}")
        print(f"ANIMAL SPECIES   : {self.animal_type}")
        print(f"REGION/DISTRICT  : {self.district}")
        print("HEALTH TIMELINE  :")
        if not self.health_history:
            print("  No health checks recorded yet.")
        else:
            for status, weight, vax, date_recorded in self.health_history:
                
                print(f"  - [{date_recorded}] Condition: {status} | Weight: {weight}kg | {vax}")
        print("-" * 60)

    # CLASS METHOD TO ACCESS TOTAL COUNT ON LIVESTOCK
    @classmethod
    def get_total_livestock_count(cls) -> int:
        
        return cls.total_livestock_count

    @classmethod
    def create_anonymous_livestock(cls, count_index: int, animal_type: str, district: str):
        
        generated_tag = f"AGR-DPG-{count_index:04d}"
        return cls(generated_tag, animal_type, district)

    # STATIC METHOD FOR FORMAT VALIDATION
    @staticmethod
    def validate_farm_tag(tag_id: str) -> bool:
        
        return tag_id.startswith("AGR-DPG-") and len(tag_id) == 12



# DATA STRUCTURE CONTAINER FOR LIVESTOCK MANAGEMENT
class AgriculturalTrackerSystem:

    def __init__(self):
        
        self.livestock_db: dict[str, LivestockRecord] = {}

    def register_livestock(self, animal_obj: LivestockRecord) -> None:
        
        if LivestockRecord.validate_farm_tag(animal_obj.tag_id):
            self.livestock_db[animal_obj.tag_id] = animal_obj
            print(f"[SYSTEM] Livestock {animal_obj.tag_id} successfully added to central database.")
        else:
            print(f"[SYSTEM ERROR] Invalid Tag format '{animal_obj.tag_id}'. Standard format required.")

    def display_all_records(self) -> None:
       
        print("\n--------------- ALL REGISTERED LIVESTOCK ---------------")
        if not self.livestock_db:
            print("Database is empty.")
            return

        for tag_id, record in self.livestock_db.items():
            record.display_info()




if __name__ == "__main__":
    print("=== DPG AGRICULTURAL TRACKING SYSTEM INITIALIZING ===\n")

   
    crop_rice = FarmCrop("PLOT-01", "NERICA Rice", 2.5)
    crop_cassava = FarmCrop("PLOT-02", "Cassava", 1.0)

    crop_rice.add_harvest_yield(1200.0)
    crop_rice.add_harvest_yield(800.0)
    crop_cassava.add_harvest_yield(450.0)

    print("\n--- CROP YIELD SUMMARY ---")
    crop_rice.display_crop_summary()
    crop_cassava.display_crop_summary()

   
    animal1 = LivestockRecord("AGR-DPG-0001", "Cattle (N'Dama)", "Bombali District")
    animal2 = LivestockRecord.create_anonymous_livestock(2, "West African Dwarf Goat", "Kono District")

   
    system = AgriculturalTrackerSystem()
    print("\n--- REGISTERING LIVESTOCK IN DICTIONARY DATABASE ---")
    system.register_livestock(animal1)
    system.register_livestock(animal2)

   
    print("\n--- LOGGING HEALTH ASSESSMENTS (TUPLE DATA STRUCTURE) ---")
    animal1.log_health_check(status="Healthy", weight_kg=250.5, vaccinated=True)
    animal1.log_health_check(status="Routine Check", weight_kg=258.0, vaccinated=True)
    
    animal2.log_health_check(status="Underweight", weight_kg=22.0, vaccinated=False)

    
    print("\n--- UPDATING RECORD DEMO ---")
    animal2.update_record(district="Bo District")

    
    system.display_all_records()

   
    print("\n--- CLASS & STATIC METHOD VERIFICATIONS ---")
    print(f"Total Registered Animals (Class Method): {LivestockRecord.get_total_livestock_count()}")
    
    check_id = "AGR-DPG-0001"
    valid_flag = LivestockRecord.validate_farm_tag(check_id)
    print(f"Static Method Check - Is '{check_id}' valid DPG ID? -> {valid_flag}")