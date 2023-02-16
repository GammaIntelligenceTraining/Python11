import os

files = os.walk('needs_sorting')

for folder in ['images', 'text', 'music']:
    if not os.path.isdir(folder):
        os.mkdir(folder)

for d, dn, fn in files:
    for name in fn:
        file_path = os.path.splitext(name)[1]
        if file_path == '.png' or file_path == '.jpg':
            os.rename(f'needs_sorting/{name}', f'images/{name}')
        elif file_path == '.txt' or file_path == '.html':
            os.rename(f'needs_sorting/{name}', f'text/{name}')
        elif file_path == '.mp3':
            os.rename(f'needs_sorting/{name}', f'music/{name}')