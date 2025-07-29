
import os
import json
import re

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def extract_filtered_json(input_dir="downloads_final"):
    selected_fields = ["title", "description", "duration", "upload_date", "view_count", "like_count", "tags"]

    for subdir in os.listdir(input_dir):
        sub_path = os.path.join(input_dir, subdir)
        if os.path.isdir(sub_path):
            for file in os.listdir(sub_path):
                if file.endswith(".json") and not file.endswith("_filtered.json"):
                    json_path = os.path.join(sub_path, file)

                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    filtered = {k: data.get(k, None) for k in selected_fields}

                    # Save filtered JSON with _filtered suffix
                    base_name = os.path.splitext(file)[0]
                    filtered_filename = f"{base_name}_filtered.json"
                    filtered_path = os.path.join(sub_path, filtered_filename)

                    with open(filtered_path, 'w', encoding='utf-8') as f_out:
                        json.dump(filtered, f_out, ensure_ascii=False, indent=4)

                    print(f"✅ Saved filtered JSON for: {base_name}")

# Run it
extract_filtered_json()
