import argparse

def extract_features_from_geojson(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        start_idx = content.find('"features": [') + len('"features": [')
        end_idx = content.rfind(']')
        
        # featuresの中身だけを抽出
        return content[start_idx:end_idx]

def merge_geojson_files(files, output_path):
    # 最初のファイルからヘッダーを取得
    with open(files[0], 'r', encoding='utf-8') as file:
        content = file.read()
        header = content[:content.find('"features": [') + len('"features": [')]

    # featuresを結合
    features_list = [extract_features_from_geojson(file) for file in files]
    # 空の要素をフィルタリング
    features_list = [f for f in features_list if f.strip()]
    # featuresをカンマで結合
    merged_features = ','.join(features_list)

    # フッターを追加
    footer = "]}"
    
    # マージした内容を出力
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(header + merged_features + footer)




def main():
    parser = argparse.ArgumentParser(description="Merge multiple GeoJSON files into one.")
    parser.add_argument('files', type=str, nargs='+', help="GeoJSON files to merge")
    parser.add_argument('-o', '--output', required=True, help="Output file name")
    args = parser.parse_args()

    merge_geojson_files(args.files, args.output)

if __name__ == "__main__":
    main()
