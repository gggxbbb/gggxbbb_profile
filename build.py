from jinja2 import Template
import requests

repos = requests.get('https://api.github.com/users/gggxbbb/repos').json()

own_repos = []

for repo in repos:
    own_repos.append({
        'name': repo['full_name'],
        'url': repo['html_url'],
        'description': repo['description'] or "暂无描述",
        'language': repo['language'] or "未知语言",
        'stars': repo['stargazers_count'],
        'forks': repo['forks_count'],
        'updated': repo['updated_at'],
    })

own_repos = sorted(own_repos, key=lambda k: k['updated'], reverse=True)
own_repos = own_repos[:3]

temp = Template(open('temp.html', encoding='utf-8').read())
opt = temp.render(repos=own_repos)
open('dist/index.html', 'w', encoding='utf-8').write(opt)
