
import csv


def add_link_column_native(csv_file_path, output_file_path=None):
    """
    Fügt Link-Spalte mit nativen Python CSV-Funktionen hinzu
    """
    
    if output_file_path is None:
        output_file_path = csv_file_path.replace('.csv', '_with_links.csv')
    
    with open(csv_file_path, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=';')
        
        # Header mit neuer 'link' Spalte
        fieldnames = reader.fieldnames + ['link_bilder']
        
        with open(output_file_path, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            
            for row in reader:
                # Link basierend auf ID hinzufügen
                row['link_bilder'] = f"http://localhost:5000/api/{row['id']}/raw"
                writer.writerow(row)
    

if __name__ == "__main__":
    input_file = "export_start_29_9_2025_end_2_10_2025.csv"
    add_link_column_native(input_file)