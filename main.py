def move(disc , source, destination, aux):
    if disc >0:
        move(disc-1,source,aux,destination)
        print("Disc "+ str(disc)+ ": move from "+ str(source) + " to "+str(destination))
        move(disc-1,aux,destination,source)
        
move(5,"Left","Middle","Right")
        