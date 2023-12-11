from pprint import pprint
movie_info={
    1:{
        'name':'Sam Bahadur',
        'show_time':'9:20am',
        'ticket_price':{'Standard':180,
                        'Luxury':240,
                        'Royal':360},
        'no_of_seats':[80,15,8]
    },
    2:{
        'name':'Dunki',
        'show_time':'10:30pm',
        'ticket_price':{'Standard':180,
                        'Luxury':240,
                        'Royal':360},
        'no_of_seats':[70,13,6]
    },
    3:{
        'name':'Animal',
        'show_time':'9:40am',
        'ticket_price':{'Standard':180,
                        'Luxury':240,
                        'Royal':360},
        'no_of_seats':[130,26,12]
    },
    4:{
        'name':'12th Fail',
        'show_time':'3:20pm',
        'ticket_price':{'Standard':180,
                        'Luxury':240,
                        'Royal':360},
        'no_of_seats':[67,5,14]
    }
    
}
class Movie:
    def __init__(self) -> None:
        self.name=''
        self.show_time=''
        self.ticket=0
        self.no_of_tickets=0
        self.show()
        self.display()
    
    def show(self): 
        print("Movies Available")
        for i in movie_info.keys():
            print(f'{i}.{movie_info[i]["name"]}')
        print('\n')
        no=int(input("Select a movie by number(1/2/3/4):"))
        self.name=movie_info[no]["name"]
        print(movie_info[no])
        self.no_of_tickets=int(input("How many people?"))
        self.show_time=movie_info[no]['show_time']
        tick=input('Select type of seat(S/L/R)')
        if tick.upper()=='L' or tick.upper()=='LUXURY' and movie_info[no]['no_of_seats'][1]>0:
            movie_info[no]['no_of_seats'][1]-=self.no_of_tickets
            self.ticket+=movie_info[no]['ticket_price']['Luxury']
        elif tick.upper()=='R' or tick.upper()=='ROYAL' and movie_info[no]['no_of_seats'][2]>0:
            movie_info[no]['no_of_seats'][2]-=self.no_of_tickets
            self.ticket+=movie_info[no]['ticket_price']['Royal']
        else:
            if movie_info[no]['no_of_seats'][0]>0:
                movie_info[no]['no_of_seats'][0]-=self.no_of_tickets
                self.ticket+=movie_info[no]['ticket_price']['Standard']
        self.ticket*=self.no_of_tickets
                
    def display(self):
        print('\n\nFinal Bill\n')
        print(f'Name:{self.name}\nTime:{self.show_time}\nNo. of tickets:{self.no_of_tickets}\nPrice:${self.ticket}')
           
m=Movie()
            
        
