import xml.etree.ElementTree as ET
import json


xml_file = "C:/Users/Arda/Desktop/DSA PROJECT/export.xml"

try:

    tree = ET.parse(xml_file)
    root = tree.getroot()

    step_data = []

    for record in root.findall("Record"):
        if record.attrib.get("type") == "HKQuantityTypeIdentifierStepCount":
            step_data.append({
                "startDate": record.attrib.get("startDate"),
                "endDate": record.attrib.get("endDate"),
                "value": record.attrib.get("value")
            })

   
    json_file = "step_count_data.json"  
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(step_data, f, indent=4)

    print(f"Adım sayısı JSON dosyası başarıyla oluşturuldu: {json_file}")

except FileNotFoundError:
    print("Hata: export.xml dosyası bulunamadı. Lütfen dosya yolunu kontrol edin.")
except ET.ParseError:
    print("Hata: XML dosyası parse edilemedi. Lütfen dosyanın doğru formatta olduğundan emin olun.")
