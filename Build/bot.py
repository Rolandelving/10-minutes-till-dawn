# Create a simple download script
python -c "
import requests
from pathlib import Path

base_url = 'https://nexusapp.neocities.org/moderngame/projects/10-minutes-till-dawn/Build/'
files = [
    '10MinutesTillDawnWebGL.wasm.code.unityweb',
    '10MinutesTillDawnWebGL.data.unityweb'
]

output_dir = Path('unity_assets/nexusapp.neocities.org/moderngame/projects/10-minutes-till-dawn/Build')
output_dir.mkdir(parents=True, exist_ok=True)

for filename in files:
    print(f'Downloading {filename}...')
    try:
        response = requests.get(base_url + filename, timeout=120)
        if response.status_code == 200:
            file_path = output_dir / filename
            file_path.write_bytes(response.content)
            size_mb = len(response.content) / (1024 * 1024)
            print(f'✅ Downloaded: {filename} ({size_mb:.2f} MB)')
        else:
            print(f'❌ Failed to download {filename}: {response.status_code}')
    except Exception as e:
        print(f'❌ Error downloading {filename}: {e}')
"