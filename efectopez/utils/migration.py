import shutil


def migrate_templates(base_path: str, app_name: str):
    src = f'{base_path}/{app_name}/templates/{app_name}'
    dst = f'{base_path}/templates/{app_name}'
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)
    print(f'{app_name} templates migration finished.')


def migrate_static(base_path: str, app_name: str):
    src = f'{base_path}/{app_name}/static/'
    dst = f'{base_path}/static/'
    # shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)
    print(f'{app_name} static migration finished.')
