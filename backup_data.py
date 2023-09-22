def backup_csv_data(output_path,date_string=''):
    import shutil
    from pathlib import Path
    import read_data

    backup_data_path = read_data.read_backup_data_directory(date_string)
    original_data_path = read_data.read_data_directory(date_string)
    csp = str(Path.cwd())

    original_path = original_data_path+"/" + output_path
    target_path = backup_data_path+"/" + output_path

    original_path = original_path.lstrip('/')
    original_path = original_path.replace('/', '\\')

    target_path = target_path.lstrip('/')
    target_path = target_path.replace('/', '\\')

    original = csp + "\\"+original_path
    target = csp + "\\"+target_path
    try:
        shutil.copyfile(original, target)
    except Exception:
        print("[ERROR]: Backup Error: "+str(Exception))
