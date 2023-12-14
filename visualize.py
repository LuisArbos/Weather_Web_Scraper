from tabulate import tabulate

def print_table_info(data):
    sorted_data = sorted(data, key=lambda x: x['city'])
    headers = sorted_data[0].keys()
    table = tabulate([item.values() for item in sorted_data], headers=headers, tablefmt='grid')
    print(table)
    