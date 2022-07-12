def main():
    #Declare variables
    #list of strings;artist
    #list of strings:album
    artist=["","","",""]
    album=["","","",""]
    #lists of ints
    release_date=[0,0,0,0]
    records_sold=[0,0,0,0]
    count_year=0
    sold_count=0
    outfile=open('albums.txt',"r")
    print('Artist\tAlbum\tRelease date\tRecords Sold\n')
    print('-----------------------------------------------\n')
    for n in range(5):
        line1=infile.readline()
        #split data into four fields
        artists=line1.split(',')
        if int(artists[2])<2000:
           count_year=count_year+1
        if int(artists[3])>2500000
            sold_count=sold_count+1
        print(f"{:<10}{:<20}{:<10}{:<20}".format(artist[0],artists[1],artists[2],artists[3))
        print("Records sold before 2000:2")
        print("Records sold over $2,500,000:3")
main()
