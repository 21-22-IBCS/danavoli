from graphics1 import*
from Button import*



def main():

    win = GraphWin (" Coffee budget ", 800, 600)
    coffeetext = Text(Point (400,100), "Save your coffee spendings!")
    coffeetext.setSize(30)
    coffeetext.draw(win)
    coffeetext2 =Text(Point (400,220), "Your Options: Starbucks, Lander, Anthem, Olympia")
    coffeetext2.setSize(20)
    coffeetext2.draw(win)
    file = open("starbucksmenu.txt", "r")
    text = file.read(99 - 0)
    file2 = open("lander.txt", "r")
    text1 = file2.read(150 - 0)
    file3 = open("anthem.txt", "r")
    text2 = file3.read(800 - 0)
    file4 = open("olympia.txt", "r")
    text3 = file4.read(500 - 0)
    file5 = open("monday.txt", "r")
    text4 = file5.read(50 - 0)
    file6 = open("wednesday.txt", "r")
    text5 = file6.read(50 - 0)
    file7 = open("friday.txt", "r")
    text6 = file7.read(55 - 0)
    file8 = open("sunday.txt", "r")
    text7 = file8.read(55 - 0)
    
    
    
    
    
    

    coffee = Image(Point(400,400), "coffeecup.png")
    coffee.draw(win)

    e = Entry(Point(350,300), 40)
    step = Button(win, "cyan", "Add", Point(550, 300), 30)
    quit = Button(win, "grey", "Quit", Point(65, 550), 30)
    day = Button(win, "white", "Pick a Day!", Point(720, 525), 50)
    e.draw(win)



    
    d = ""

    while True:
        m1 = win.getMouse()
        
        
        
        if step.isClicked(m1):
            d = e.getText()
            
        if day.isClicked(m1):
            win10 = GraphWin("what day", 800, 600)
            monday = Button(win10, "red", "Monday", Point(150, 230), 60)
            wednesday = Button(win10, "grey", "Wednesday", Point(320, 230), 60)
            friday = Button(win10, "white", "Friday", Point(490, 230), 60)
            sunday = Button(win10, "green", "Sunday", Point(660, 230), 60)
            newtext = Text(Point(400, 300), " ")
            newtext.setText(text)
            title = Text(Point(400, 100), "Pick a day and see your budget!")
            title.setSize(25)
            title.draw(win10)

            enjoy = Image(Point(400, 450), "logo3.png")
            enjoy.draw(win10)

            while True:
                 m6 = win10.getMouse()

                 if monday.isClicked(m6):
                     win11 = GraphWin("Your Budget", 350, 200)
                     coffeestar5 = Text(Point (180,90), " " )
                     coffeestar5.setText(text4)
                     coffeestar5.draw(win11)

                 if wednesday.isClicked(m6):
                     win12 = GraphWin("Your Budget", 350, 200)
                     coffeestar6 = Text(Point (180,90), " " )
                     coffeestar6.setText(text5)
                     coffeestar6.draw(win12)
                     
                 if friday.isClicked(m6):
                     win13 = GraphWin("Your Budget", 350, 200)
                     coffeestar7 = Text(Point (180,90), " " )
                     coffeestar7.setText(text6)
                     coffeestar7.draw(win13)
                     
                 if sunday.isClicked(m6):
                     win14 = GraphWin("Your Budget", 350, 200)
                     coffeestar8 = Text(Point (180,90), " " )
                     coffeestar8.setText(text7)
                     coffeestar8.draw(win14)

                     


                     


                     


            
            
            

            

     
 
            
            

        if "Starbucks" in d:
            win2 =  GraphWin (" what coffee ", 800, 600)
            coffeestar = Text(Point (400,300), " " )
            coffeestar.setText(text)
            menutext = Text(Point(530,130), "Click for the Starbucks menu!")
            menutext.setSize(30)
            menutext.draw(win2)
    
            
            
            starbucks = Button(win2, "green", "Starbucks Coffee", Point(500,250), 70)
            starbie = Image(Point(230, 250), "sbx2.png")
            starbie.draw(win2)
    

            while True:
                m2 = win2.getMouse()
                if starbucks.isClicked(m2):
                    win3 = GraphWin("Menu Starbucks", 500, 300)
                    coffeestar = Text(Point (200,50), " " )
                    coffeestar.setText(text)
                    coffeestar.draw(win3)

        #if "" in d:
            #win2 =  GraphWin (" what coffee ", 800, 600)
            #coffeestar = Text(Point (400,300), " " )
            #coffeestar.setText(text)
            
           # starbucks = Button(win2, "cyan", "starbucks coffee", Point(550, 300), 70)
            #lander = Button(win2, "cyan", "lander coffee", Point(250, 300), 70)
                    
                    

        if "Lander" in d:
            win4 = GraphWin("what coffee", 800, 600)
            coffeestar1 = Text(Point (400,300), " " )
            coffeestar1.setText(text)
            menutext1 = Text(Point(400,130), "Click for the  Lander menu!")
            menutext1.setSize(30)
            menutext1.draw(win4)

            lander = Button(win4, "yellow", "Lander Coffee", Point(400, 250), 70)
            drink = Image(Point(200, 400), "drink1.png")
            drink.draw(win4)

            while True:
                m3 = win4.getMouse()
                if lander.isClicked(m3):
                    win5 = GraphWin("Menu Lander", 500, 300)
                    coffeestar2 = Text(Point (200,100), " " )
                    coffeestar2.setText(text1)
                    coffeestar2.draw(win5)
                    
        if "Anthem" in d:
            win6 = GraphWin("what coffee", 800, 600)
            coffeestar3 = Text(Point (400,300), " " )
            coffeestar3.setText(text)
            menutext2 = Text(Point(400,130), "Click for the Anthem menu!")
            menutext2.setSize(30)
            menutext2.draw(win6)

            anthem = Button(win6, "grey", "Anthem Coffee", Point(400, 250), 70)
            drink2 = Image(Point(170, 400), "drink2.png")
            drink2.draw(win6)

            while True:
                m4 = win6.getMouse()
                if anthem.isClicked(m4):
                    win7 = GraphWin("Menu Anthem", 650, 450)
                    coffeestar3 = Text(Point (300,200), " " )
                    coffeestar3.setText(text2)
                    coffeestar3.draw(win7)

        if "Olympia" in d:
            win8 = GraphWin("what coffee", 800, 600)
            coffeestar4 = Text(Point (400,300), " " )
            coffeestar4.setText(text)
            menutext3 = Text(Point(520,130), "Click for the Olympia menu!")
            menutext3.setSize(30)
            menutext3.draw(win8)

            olympia = Button(win8, "orange", "Olympia Coffee", Point(520, 250), 70)
            drink3 = Image(Point(170, 400), "drink3.png")
            drink3.draw(win8)

            while True:
                m5 = win8.getMouse()
                if olympia.isClicked(m5):
                    win9 = GraphWin("Menu Olympia", 650, 450)
                    coffeestar4 = Text(Point (300,200), " " )
                    coffeestar4.setText(text3)
                    coffeestar4.draw(win9)
                    

            


            
                    
            


        if quit.isClicked(m1):
            win.close()
            break

        
            
            
            
            
            
            
    

if __name__=="__main__":
    main()
