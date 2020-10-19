myfile = 'video-001'
prefix = 'video-'

if myfile.startswith(prefix):
    prefix_len = len(prefix) #6
    print(myfile[prefix_len:])

print(myfile.removeprefix(prefix))

print(myfile.removesuffix('001'))