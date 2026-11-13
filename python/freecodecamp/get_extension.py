def get_extension(filename):

    return filename.split('.')[-1]  if '.' in filename and not filename.endswith('.') else 'none'
