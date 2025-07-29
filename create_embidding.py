import os
import json
import re
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import numpy as np

def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def generate_embeddings(input_dir="downloads_final", model_name='all-MiniLM-L6-v2', target_dim=64):
    model = SentenceTransformer(model_name)

    all_texts = []
    file_paths = []

    # Step 1: Collect all text for fitting PCA
    for subdir in os.listdir(input_dir):
        sub_path = os.path.join(input_dir, subdir)
        if os.path.isdir(sub_path):
            for file in os.listdir(sub_path):
                if file.endswith("_filtered.json"):
                    file_path = os.path.join(sub_path, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                    desc = data.get('description') or ''
                    tags = data.get('tags') or []
                    tag_str = ' '.join(tags)
                    combined = f"{desc} {tag_str}".strip()

                    if combined:
                        all_texts.append(combined)
                        file_paths.append(file_path)
    print(f"Collected {len(all_texts)} texts for embedding generation.")
    # Step 2: Get original embeddings
    original_embeddings = model.encode(all_texts)
    print("generated original embeddings")
    # # Step 3: Reduce to 64-dim using PCA
    # pca = PCA(n_components=64)
    # reduced_embeddings = pca.fit_transform(original_embeddings)
    # print(reduced_embeddings.shape)
    # Step 4: Save each embedding back into its JSON file
    for i, file_path in enumerate(file_paths):
        print(i)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        data['embedding'] = original_embeddings[i].tolist()

        with open(file_path, 'w', encoding='utf-8') as f_out:
            json.dump(data, f_out, ensure_ascii=False, indent=4)

        print(f"✅ Added 64-dim embedding to: {file_path}")

# Run it
generate_embeddings()
