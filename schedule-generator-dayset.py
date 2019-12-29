import datetime

FILENAME = 'schedule.txt'

DATE_FORMAT = '%d %b %Y'
DATE_WIDTH = 12
ALTERNATIVES = ('D | S => D | S', )
LEN_OF_ALTERNATIVES = len(ALTERNATIVES)

DATES_DELIMITER = ' - '
COLUMNS_DELIMITER = ' : '

LEFT_COLUMN_HEADER = 'dayset'
RIGHT_COLUMN_HEADER = '  assignment'

def make_header(left_column_header, right_column_header, schedule_file):
    schedule_file.write(f"{left_column_header:^{DATE_WIDTH*2 + len(DATES_DELIMITER)}}{COLUMNS_DELIMITER}{right_column_header}\n")

def make_checkpoint(first_date, second_date, alternative, schedule_file):
    schedule_file.write(f"{first_date.strftime(DATE_FORMAT):>{DATE_WIDTH}}{DATES_DELIMITER}"\
          f"{second_date.strftime(DATE_FORMAT):<{DATE_WIDTH}}{COLUMNS_DELIMITER}{alternative}\n")

def generate(start, end, step = 3, interval = 1):
    index = 0
    with open(FILENAME, 'w+') as schedule_file:
        make_header(LEFT_COLUMN_HEADER, RIGHT_COLUMN_HEADER, schedule_file)
        while start <= end:
            make_checkpoint(start, start + datetime.timedelta(days = step), ALTERNATIVES[index % LEN_OF_ALTERNATIVES], schedule_file)
            start += datetime.timedelta(days = step + interval)
            index += 1

def main():
    now = datetime.date(2020, 1, 11)#datetime.datetime.now()
    generate(start = now, end = now + datetime.timedelta(days = 365))

if __name__ == '__main__':
    main()
