import os


def get_files_with_ext(ext):
    docu=[]
    for fichero in contenido:
        if os.path.isfile(os.path.join(desk, fichero)) and fichero.endswith(ext):
            docu.append(fichero)
    return docu
def create_directs(desk):
  #  desk = "C:\\Users\\ilias\\Downloads"
    dirs=[]
    for archivo in contenido:
        nombre, extension = os.path.splitext(archivo)
        dd=extension[1:]
        dirs.append(dd)
    for dir_3 in dirs:
        if ((os.path.exists(desk+"\\"+dir_3)) == bool(False)):
           os.mkdir(desk+"\\"+dir_3)

desk="C:\\Users\\ilias\\OneDrive\\Imágenes" # here change your directory
desk=input("give me the directory")
contenido=os.listdir(desk)
extensiones=[]
create_directs(desk)

print(contenido)

for archivo in contenido:
    nombre, extension = os.path.splitext(archivo)
    print(get_files_with_ext(extension))
    extensiones.append(extension)

for ll in extensiones:
    files_to_copy=get_files_with_ext(ll)
    for cut in files_to_copy:
        os.rename(desk + "\\" + cut, desk + "\\" +ll[1:]+"\\"+cut)

print(extensiones)
create_directs(desk)