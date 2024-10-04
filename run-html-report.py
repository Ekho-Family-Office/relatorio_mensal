import sys
import locale
from datetime import datetime, timedelta

# Set the locale to Brazilian Portuguese
locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')


def generate_report(file_number):


    # Read the content of the template file
    with open('template-wolf.html', 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the placeholders with the specified values
    content = content.replace('{{NAME}}', 'CARLOS EDUARDO SILVA DE ALMEIDA MOYSES')

    # Get the current date and subtract one month
    previous_month_date = datetime.now().replace(day=1) - timedelta(days=1)

    # Get the month name and capitalize the first letter
    previous_month_name = previous_month_date.strftime('%B').upper()

    content = content.replace('{{MES}}', previous_month_name )
    content = content.replace('%PATRIMONIOGLOBAL%', 'R$ 109.235.144,69')
    content = content.replace('{{REND}}', 'R$ 1.124.002,71')
    content = content.replace('{{REND_PER}}', '4,56%')

    # Create the new filename using the parameter
    new_filename = f'report-{file_number}.html'

    # Write the modified content to the new file
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(content)

    print(f'Report generated: {new_filename}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_number>")
    else:
        file_number = sys.argv[1]
        generate_report(file_number)




