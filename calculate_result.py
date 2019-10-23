from operator import itemgetter


class MonthlyComputingResults:
    """
    This class takes the objects from list and computing monthly results
    """

    def getting_monthly_record(self,record,arguments):
        
        calculating_records = []
        year = str(arguments.year)
        month = str(arguments.month)
        calculating_records = [getting_dictionaries 
                                for getting_dictionaries in record
                                for dic_values in getting_dictionaries.values() 
                                if dic_values.startswith(f"{year}-{month}")]
        
        return calculating_records

    def get_temperature_averages(self,monthly_record):
        max_temperature = [int(subset['Max TemperatureC']) for subset in monthly_record]
        min_temperature = [int(subset['Min TemperatureC']) for subset in monthly_record]
        mean_humidty = [int(subset[' Mean Humidity']) for subset in monthly_record]
        max_average = sum(max_temperature) // len(monthly_record) 
        min_average = sum(min_temperature) // len(monthly_record)
        humidity_average = sum(mean_humidty) // len(monthly_record)
        
        print("Maximum Average Temperature:", max_average, "C")
        print("Minimum Average Temperature:", min_average, "C")
        print("Mean Humidity Average:", humidity_average, "%")
    

class YearlyComputingResults:
    """
    This class takes the objects from list and computing yearly results
    """

    def getting_yearly_record(self,record,arguments):
        calculating_records = []
        year = str(arguments.year)

        calculating_records = [getting_dictionaries 
                                for getting_dictionaries in record
                                for dic_values in getting_dictionaries.values() 
                                if dic_values.startswith(f"{year}")]
        

        return calculating_records

    def get_temperature_averages(self,yearly_record):
        max_temperature = [int(subset['Max TemperatureC']) for subset in yearly_record]
        min_temperature = [int(subset['Min TemperatureC']) for subset in yearly_record]
        mean_humidty = [int(subset[' Mean Humidity']) for subset in yearly_record]
        pkt = [subset['PKT'] for subset in yearly_record] or [subset['PKST'] for subset in yearly_record]
        max_merge = list(zip(max_temperature,pkt))
        highest_temperature_result = max(max_merge,key=itemgetter(0))
        min_merge = list(zip(min_temperature,pkt))
        lowest_temperature_result = min(min_merge,key=itemgetter(0))
        humidity_merge = list(zip(mean_humidty,pkt))
        highest_humidity_result = max(humidity_merge,key=itemgetter(0))

        print("Highest Temperature And Day: ", highest_temperature_result)
        print("Lowest Temperature And Day: ", lowest_temperature_result)
        print("Max Humidity And Day: ", highest_humidity_result)
        