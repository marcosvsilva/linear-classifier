import requests
import csv

def download_csv(url, file):
    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        
        with open(file, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            rows = content.split('\n')
            
            for row in rows:
                columns = row.split(',')
                csv_writer.writerow(columns)
                
        return True
    else:
        return False
