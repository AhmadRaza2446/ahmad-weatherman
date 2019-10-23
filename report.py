from datetime import datetime

class MonthlyReport:
    """
    This class takes the objects from list and draw multiline chart on console
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
    
    def monthly_chart(self,req_objects):
        COLOR_BLUE = '\033[1;34;48m'
        COLOR_RED = '\033[1;31;48m'
        max_temperature = [int(subset['Max TemperatureC']) for subset in req_objects]
        min_temperature = [int(subset['Min TemperatureC']) for subset in req_objects]
        pkt = [subset['PKT'] for subset in req_objects] or [subset['PKST'] for subset in req_objects]
        pick_date = pkt[0]
        convert_listdate_to_datetime = datetime.strptime(pick_date, '%Y-%m-%d')
        get_monthname_year = convert_listdate_to_datetime.strftime('%B %Y')
        print(get_monthname_year)

        for pkt,max_temp,min_temp in zip(pkt,list(max_temperature),list(min_temperature)):

            print(f"{pkt}{COLOR_RED.format('+' * max_temp)} {max_temp}C")
            print(f"{pkt}{COLOR_BLUE.format('+' * min_temp)} {min_temp}C")

                    
class MonthlyBonusReport:
    """
    This class takes the objects from list and draw single line chart on console
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
    
    def bonus_chart(self,req_objects):
        COLOR_BLUE = '\033[1;34;48m'
        COLOR_RED = '\033[1;31;48m'
        max_temperature = [int(subset['Max TemperatureC']) for subset in req_objects]
        min_temperature = [int(subset['Min TemperatureC']) for subset in req_objects]
        pkt = [subset['PKT'] for subset in req_objects] or [subset['PKST'] for subset in req_objects]
        pick_first_date = pkt[0]
        convert_listdate_to_datetime = datetime.strptime(pick_first_date, '%Y-%m-%d')
        get_monthname_year = convert_listdate_to_datetime.strftime('%B %Y')
        print(get_monthname_year)

        for pkt,max_temp,min_temp in zip(pkt,list(max_temperature),list(min_temperature)):

            print(f"{pkt}{COLOR_RED.format('+' * max_temp)} "
            f"{COLOR_BLUE.format('+' * min_temp)}{max_temp}C-{min_temp}C")
