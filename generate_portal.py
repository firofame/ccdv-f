import json

with open('curriculum.json', encoding='utf-8') as f:
    data = json.load(f)

curriculum_json = json.dumps(data)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

prefix = 'const CURRICULUM = '
start = html.find(prefix)
if start == -1:
    raise SystemExit('CURRICULUM marker not found in index.html')
start += len(prefix)
state_marker = ';\n\n    // State'
end = html.find(state_marker, start)
if end == -1:
    raise SystemExit('State marker not found after CURRICULUM in index.html')

new_html = html[:start] + curriculum_json + html[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Successfully verified and updated index.html from curriculum.json!')
