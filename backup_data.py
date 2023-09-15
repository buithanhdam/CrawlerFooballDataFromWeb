def backup_csv_data(output_path):
    import shutil
    from pathlib import Path

    csp = str(Path.cwd())
    original = csp + "/" + output_path
    target = csp + "/backup/" + output_path
    try:
        shutil.copyfile(original, target)
    except NameError:
        print("Backup Error: "+NameError)
