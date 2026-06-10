import os
import csv
import qrcode

def generate_gym_qrs():
    csv_file_path = 'gym_data.csv'
    output_dir = 'gym_qr_codes'
    base_url = 'https://ELHasssen1722.pythonanywhere.com/machine/'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            machine_id = row['id']
            machine_name = row['machine_name'].replace('/', '-').replace(' ', '_').lower()
            
            full_url = f"{base_url}{machine_id}"
            
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(full_url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            file_name = f"{machine_id}_{machine_name}.png"
            file_path = os.path.join(output_dir, file_name)
            img.save(file_path)
            
    print(f"[✓] Success: 29 QR codes have been generated inside the '{output_dir}' folder!")

if __name__ == '__main__':
    generate_gym_qrs()