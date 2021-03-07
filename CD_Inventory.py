#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# STimchenko, 2021-Mar-06, Incorporated TODO tasks
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt' # text storage file 
lstOfCDObjects = [] # list of lists to hold data
table = [] #list to manage data
strChoice = '' # User input
dicRow = {} #dictonary of data row
objFile = None # file object

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    # -- Fields -- #
    cd_id = int
    cd_title = str
    cd_artist = str
    
    # -- Constructor -- #
    def __init__(self, cdid, ttl, art):
        # -- Attributes -- #
        self.__cd_id = cdid
        self.__cd_title = ttl
        self.__cd_artist = art
    
    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id.title()
    
    @cd_id.setter
    def cd_id(self, value):
        if not str(value).isnumeric():
            raise Exception('The track number must be a digit.')
        else:
            self.__cd_id = value
    
    @property
    def cd_title(self):
        return self.__cd_title.title()
    
    @cd_title.setter
    def cd_title(self, value):
        if not value:
            raise Exception('A title is required.')
        else:
            self.__cd_title = value
            
    @property
    def cd_artist(self):
        return self.__cd_artist.title()
    
    @cd_artist.setter
    def cd_artist(self, value):
        if not value:
            raise Exception('An artist is required.')
        else:
            self.__cd_artist = value


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    # -- Methods -- #
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Function to manage data output to file from a list of dictionaries
        
        Writes the table data to file identified as file_name from a 2D table.
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        Args:
            file_name (string): name of file used to write data to
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        
        Returns:
            None.
        
        """
        strYesNo = IO.save_inventory()
        if strYesNo == 'y':
            objFile = open(file_name, 'w')
            for row in lst_Inventory:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries
        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        Args:
            file_name (string): name of file used to read the data from
        Returns:
            table (list of dict): the inventory of the text file
        
        """
        try:
            objFile = open(file_name, 'r')
            table.clear()
            for line in objFile:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            objFile.close()
        except FileNotFoundError:
            print("The file {} could not be loaded".format(file_name))
        return table


# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output
    
    Methods:
        print_menu(): -> (menu)
        menu_choice(): -> None
        show_inventory(table): -> (a list of CD objects)
        get_input(): -> None
        add_entry(cd_id, cd_title, cd_artist, table): -> None
        save_inventory(): -> None
        load_inventory(): -> (a list of CD objects) 
        
    """
    
    # -- Methods -- #
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
        Args:
            None.
        Returns:
            None.
       
        """
        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to File\n[x] Exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection.
        Forces selection of one of the displayed letter options.
        Args:
            None.
        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x
        
        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table.
        Allows for processing user inputs and system outputs.
        Generates feedback and confirmation messages.
        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
        Returns:
            None.
        """
        print()
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)')
        for row in lstOfCDObjects:
            print('{}\t{} ({})'.format(*row.values()))
        print('======================================')
        print()

    @staticmethod
    def get_input():
        """Collects a user input to add a CD to the current inventory table.
        Verifies that the ID is an integer and that the Title and Artist
        fields are not blank.
        
        Args:
            None.
        Returns:
            strID: the integer ID of the CD
            strTitle: the title of the CD
            strArtist: the CD artist's name
            
        """
        CDIn = CD('','','')
        # Checks for an integer input
        while True:
            try:
                CDIn.cd_id = (input('Enter ID: ').strip())
                break
            except Exception as e:
                print(e)

       # Checks for a non-empty input
        while True:
            try:
                CDIn.cd_title = input('What is the CD\'s title? ').strip()
                break
            except Exception as e:
                print(e)

        # Checks for a non-empty input
        while True:
            try:
                CDIn.cd_artist = input('What is the Artist\'s name? ').strip()
                break
            except Exception as e:
                print(e)

        return CDIn.cd_id, CDIn.cd_title, CDIn.cd_artist
        
    @staticmethod
    def add_entry(cd_id, cd_title, cd_artist, table):
        """Function to manage the addition of entries to the existing table
       
        Adds entries to the existing table after the user uses the 'a' functionality
        built into the script.
       
        Args:
            cd_id: the integer ID of the CD
            cd_title: the title of the CD
            cd_artist: the CD artist's name
           
        Returns:
            None
       
        """
        dicRow = {'ID': cd_id, 'Title': cd_title, 'Artist': cd_artist}
        table.append(dicRow)
        
    @staticmethod
    def save_inventory():
        """Writes the contents of the current inventory to file.
        
        Args:
            None.
            
        Returns:
            strYesNo: the user selection for saving.
        
        """
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        print()
        return strYesNo
    
    @staticmethod
    def load_inventory():
        """Processes the user input when loading a file.
        
        Args:
            None.
        
        Returns:
            strYes: the user response to loading the file.
        
        """
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        # Checks for a 'yes' input
        
        strYes = input('Type \'yes\' to continue and reload from file. Otherwise loading will be canceled: ').strip().lower()
        print()
        return strYes

# -- Main Body of Script -- #
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)
IO.show_inventory(lstOfCDObjects)

# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
      
    # show user current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user add data to the inventory
    elif strChoice == 'a':
        strID, strTitle, strArtist = IO.get_input()
        IO.add_entry(strID, strTitle, strArtist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        FileIO.save_inventory(strFileName, lstOfCDObjects)
        continue  # start loop back at top.
        
    # let user load inventory from file
    if strChoice == 'l':
        if IO.load_inventory() == 'yes':
            lstOfCDObjects = FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('The file was NOT loaded. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # let user exit program
    elif strChoice == 'x':
        break

