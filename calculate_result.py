from operator import itemgetter


class MonthlyComputingResults:
    """
    This class takes the objects from list and computing monthly results
    """

    def getting_monthly_record(self,record,arguments):
        
        calculating_records = []
        year = str(arguments.year)
        month = str(arguments.month)
        calculating_records = [record[getting_record_index_value] 
                                for getting_record_index_value in range(len(record))
                                for key in record[getting_record_index_value] 
                                if(record[getting_record_index_value][key].startswith(f"{year}-{month}"))]

        return calculating_records

    def get_temperature_averages(self,monthly_record):
        max_temperature = [ subset['Max TemperatureC'] for subset in monthly_record]
        min_temperature = [ subset['Min TemperatureC'] for subset in monthly_record]
        mean_humidty = [ subset[' Mean Humidity'] for subset in monthly_record]
        convert_max_list = list(map(int, max_temperature))
        sum_of_max_temperature = sum(convert_max_list)
        max_average = int(sum_of_max_temperature) // len(monthly_record)
        convert_min_list = list(map(int, min_temperature))
        sum_of_min_temperature = sum(convert_min_list)
        min_average = int(sum_of_min_temperature) // len(monthly_record)
        convert_humidity_list = list(map(int, mean_humidty))
        sum_of_mean_humidity = sum(convert_humidity_list)
        humidity_average = int(sum_of_mean_humidity) // len(monthly_record)

        print("Maximum Average Temperature:", int(max_average), "C")
        print("Minimum Average Temperature:", int(min_average), "C")
        print("Mean Humidity Average:", int(humidity_average), "%")
    

class YearlyComputingResults:
    """
    This class takes the objects from list and computing yearly results
    """


    def getting_yearly_record(self,record,arguments):
        calculating_records = []
        year = str(arguments.year)

        calculating_records = [record[getting_record_index_value] 
                                for getting_record_index_value in range(len(record))
                                for key in record[getting_record_index_value] 
                                if(record[getting_record_index_value][key].startswith(f"{year}"))]
        

        return calculating_records

    def get_temperature_averages(self,yearly_record):
        max_temperature = [ subset['Max TemperatureC'] for subset in yearly_record]
        min_temperature = [ subset['Min TemperatureC'] for subset in yearly_record]
        mean_humidty = [ subset[' Mean Humidity'] for subset in yearly_record]
        pkt = [ subset['PKT'] for subset in yearly_record] or [ subset['PKST'] for subset in yearly_record]
        convert_max_list = list(map(int, max_temperature))
        max_merge = list(zip(convert_max_list,pkt))
        highest_temperature_result = max(max_merge,key=itemgetter(0))
        convert_min_list = list(map(int, min_temperature))
        min_merge = list(zip(convert_min_list,pkt))
        lowest_temperature_result = min(min_merge,key=itemgetter(0))
        convert_humidity_list = list(map(int, mean_humidty))
        humidity_merge = list(zip(convert_humidity_list,pkt))
        highest_humidity_result = max(humidity_merge,key=itemgetter(0))

        print("Highest Temperature And Day: ", highest_temperature_result)
        print("Lowest Temperature And Day: ", lowest_temperature_result)
        print("Max Humidity And Day: ", highest_humidity_result)
    