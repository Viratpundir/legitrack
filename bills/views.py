import os
import csv
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_bills(request):
    data = []

    # 📁 Get correct file path
    file_path = os.path.join(os.path.dirname(__file__), 'sample_bills.csv')

    # 📖 Read CSV
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return Response(data)