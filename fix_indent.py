import re

with open('index.pug', 'r') as f:
    lines = f.readlines()

out = []
in_hero = False
for line in lines:
    if line.startswith('article.container.mt-3.mb-0'):
        out.append(line)
        out.append('  .row\n')
        out.append('    .col-md-12\n')
        in_hero = True
        continue
    
    if in_hero:
        if line.startswith('div.container'):
            in_hero = False
            out.append(line)
            continue
        if line.strip() == '':
            out.append(line)
        else:
            # indent by 4 spaces
            out.append('    ' + line)
    else:
        out.append(line)

with open('index.pug', 'w') as f:
    f.writelines(out)
