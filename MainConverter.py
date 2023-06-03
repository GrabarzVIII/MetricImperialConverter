import MetricToImperialConvert
import ImperialToMetricConvert

def display_menu (options):
    for index, options in enumerate(options, start=1):
        print(f'{index}. {options}')
    print('Enter option number...')

def get_choice(options):
    while True:
        try:
            display_menu(options)
            choice = int(input())
            if 1 <= choice <= len(options):
                return choice
        except ValueError:
            print('Wrnog value entered')

metric_units_list = ['mm','cm','m','km']
imperial_units_list = ['in','ft','yd','mile']

convertion_functions_dictionary = {
1 : (MetricToImperialConvert.MilimeterToInch, MetricToImperialConvert.MilimeterToFoot, MetricToImperialConvert.MilimeterToYard, MetricToImperialConvert.MilimeterToMile),
2 : (MetricToImperialConvert.CentimeterToInch, MetricToImperialConvert.CentimeterToFoot, MetricToImperialConvert.CentimeterToYard, MetricToImperialConvert.CentimeterToMile),
3 : (MetricToImperialConvert.MeterToInch, MetricToImperialConvert.MeterToFoot, MetricToImperialConvert.MeterToYard, MetricToImperialConvert.MeterToMile),
4 : (MetricToImperialConvert.KilometerToInch, MetricToImperialConvert.KilometerToFoot, MetricToImperialConvert.KilometerToYard, MetricToImperialConvert.KilmeterToMile),
5 : (ImperialToMetricConvert.InchToMilimeter, ImperialToMetricConvert.InchToCentimeter, ImperialToMetricConvert.InchToMeter, ImperialToMetricConvert.InchToKilometer),
6 : (ImperialToMetricConvert.FootToMilimeter, ImperialToMetricConvert.FootToCentimeter, ImperialToMetricConvert.FootToMeter, ImperialToMetricConvert.FootToKilometer),
7 : (ImperialToMetricConvert.YardToMilimeter, ImperialToMetricConvert.YardToCentimeter, ImperialToMetricConvert.YardToMeter, ImperialToMetricConvert.YardToKilometer),
8 : (ImperialToMetricConvert.MileToMilimeter, ImperialToMetricConvert.MileToCentimeter, ImperialToMetricConvert.MileToMeter, ImperialToMetricConvert.MileToKilometer)
}
