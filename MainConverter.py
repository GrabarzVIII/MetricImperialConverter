import MetricToImperialConvert
import ImperialToMetricConvert

def display_menu (options):
    for index, options in enumerate(options, start=1):
        print(f'{index}. {options}')
    print('Enter option number...')

def get_choice(options):
    while True:
        display_menu(options)
        choice = int(input())
        if 1 <= choice <= len(options):
            return choice
        else:
            print('Wrnog value entered')

def convertion(unit_to_convert, dimension, converted_unit):
    convertion_function_tuple = convertion_function_dictionary[unit_to_convert]
    convertion_function = convertion_function_tuple[converted_unit]
    return convertion_function(dimension)

metric_units_list = ['mm','cm','m','km']
imperial_units_list = ['in','ft','yd','mile']
end = ['End']

convertion_function_dictionary = {
1 : (MetricToImperialConvert.MilimeterToInch, MetricToImperialConvert.MilimeterToFoot, MetricToImperialConvert.MilimeterToYard, MetricToImperialConvert.MilimeterToMile),
2 : (MetricToImperialConvert.CentimeterToInch, MetricToImperialConvert.CentimeterToFoot, MetricToImperialConvert.CentimeterToYard, MetricToImperialConvert.CentimeterToMile),
3 : (MetricToImperialConvert.MeterToInch, MetricToImperialConvert.MeterToFoot, MetricToImperialConvert.MeterToYard, MetricToImperialConvert.MeterToMile),
4 : (MetricToImperialConvert.KilometerToInch, MetricToImperialConvert.KilometerToFoot, MetricToImperialConvert.KilometerToYard, MetricToImperialConvert.KilmeterToMile),
5 : (ImperialToMetricConvert.InchToMilimeter, ImperialToMetricConvert.InchToCentimeter, ImperialToMetricConvert.InchToMeter, ImperialToMetricConvert.InchToKilometer),
6 : (ImperialToMetricConvert.FootToMilimeter, ImperialToMetricConvert.FootToCentimeter, ImperialToMetricConvert.FootToMeter, ImperialToMetricConvert.FootToKilometer),
7 : (ImperialToMetricConvert.YardToMilimeter, ImperialToMetricConvert.YardToCentimeter, ImperialToMetricConvert.YardToMeter, ImperialToMetricConvert.YardToKilometer),
8 : (ImperialToMetricConvert.MileToMilimeter, ImperialToMetricConvert.MileToCentimeter, ImperialToMetricConvert.MileToMeter, ImperialToMetricConvert.MileToKilometer)
}


while True:
    print('What do you want to convert?')
    unit_to_convert = get_choice(metric_units_list + imperial_units_list + end)

    if 1 <= unit_to_convert <= len(metric_units_list + imperial_units_list + end):

        

        if 1 <= unit_to_convert <= 4:

            enter_dimension = float(input('Enter your dimension: '))

            print('Do you want to convert to?')
            converted_unit = get_choice(imperial_units_list + end)

            if converted_unit == len(metric_units_list + end):
                break

            print(convertion(unit_to_convert, enter_dimension, converted_unit))

        elif 4 < unit_to_convert <= len(metric_units_list + imperial_units_list + end) - 1:

            enter_dimension = float(input('Enter your dimension: '))

            print('Do you want to convert to?')
            converted_unit = get_choice(imperial_units_list + end)

            if converted_unit == len(metric_units_list + end):
                break

            print(convertion(unit_to_convert, enter_dimension, converted_unit))


        elif unit_to_convert == len(metric_units_list + imperial_units_list + end):
            break

    else:
        print('Wrong number entred')