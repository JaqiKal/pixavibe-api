from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Describe the structure of a database table'

    def add_arguments(self, parser):
        parser.add_argument('table_name', type=str, help='The name of the table to describe')

    def handle(self, *args, **kwargs):
        table_name = kwargs['table_name']
        with connection.cursor() as cursor:
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()

        self.stdout.write(f"Structure of table '{table_name}':")
        self.stdout.write(f"{'Column Name':<15} {'Data Type':<10} {'Not Null':<10} {'Default Value':<15} {'Primary Key':<10}")
        self.stdout.write("="*60)
        for column in columns:
            column_name = column[1] if column[1] is not None else "NULL"
            data_type = column[2] if column[2] is not None else "NULL"
            not_null = column[3] if column[3] is not None else "NULL"
            default_value = column[4] if column[4] is not None else "NULL"
            primary_key = column[5] if column[5] is not None else "NULL"
            self.stdout.write(f"{column_name:<15} {data_type:<10} {not_null:<10} {default_value:<15} {primary_key:<10}")
