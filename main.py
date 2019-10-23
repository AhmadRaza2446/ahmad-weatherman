import argparse
from datetime import datetime

from read_weather_record import RecordFile

from calculate_result import MonthlyComputingResults
from calculate_result import YearlyComputingResults

from report import MonthlyReport
from report import MonthlyBonusReport


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', type=lambda date: datetime.strptime(date, '%Y'))
    parser.add_argument('-a', type=lambda date: datetime.strptime(date, '%Y/%m'))
    parser.add_argument('-c', type=lambda date: datetime.strptime(date, '%Y/%m'))

    return  parser.parse_args()

def main():
    arguments = parse_arguments()
    
    record = RecordFile()
    weather_records = record.read_file()
    
    if arguments.a:
        
        results = MonthlyComputingResults()
        
        monthly_record = results.getting_monthly_record(weather_records,arguments.a)
        results.get_temperature_averages(monthly_record)

    if arguments.e:

        results = YearlyComputingResults()

        yearly_record = results.getting_yearly_record(weather_records,arguments.e)
        results.get_temperature_averages(yearly_record)

    if arguments.c:

        monthly_report_chart = MonthlyReport()

        getting_objects = monthly_report_chart.getting_monthly_record(weather_records,arguments.c)
        monthly_report_chart.monthly_chart(getting_objects)
        
        print("Bonus Task")

        bonus_report = MonthlyBonusReport()

        report = bonus_report.getting_monthly_record(weather_records,arguments.c)
        bonus_report.bonus_chart(report)
    
     
if __name__ == '__main__':
    main()
