import markdown
import requests


# repo config
user = "pablo-pez"
repo_name = "efectopez_blog"


def get_git_content(content_name: str = None):
    content_path = f'{content_name}'
    url = f'https://raw.githubusercontent.com/{user}/{repo_name}/main/{content_path}'
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        return response
    else:
        # print('Content was not found.')
        raise requests.exceptions.HTTPError


def list_content(content_name: str = None):
    return (item['name'] for item in get_git_content(content_name).json())


def decorate_md(html_script: str):
    html_script = html_script.replace("{abstract}", "<strong>")
    html_script = html_script.replace("{/abstract}", "</strong>")
    html_script = html_script.replace("\n", "")
    return html_script


def markdown_to_html(post_name: str):
    post_content = get_git_content(post_name).text
    # Load content and metadata
    md = markdown.Markdown(extensions=['meta'])
    html = md.convert(post_content)
    meta = md.Meta
    # html = markdown.markdown(post).replace("\n", "")
    return decorate_md(html), meta
